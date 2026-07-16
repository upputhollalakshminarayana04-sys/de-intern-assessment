import os
import pandas as pd

def load_table(folder_path, table_name):
    """Dynamically looks for CSV or Excel files matching the table name in the folder."""
    csv_path = os.path.join(folder_path, f"{table_name}.csv")
    xlsx_path = os.path.join(folder_path, f"{table_name}.xlsx")
    
    if os.path.exists(csv_path):
        print(f"Loading {table_name} from CSV...")
        return pd.read_csv(csv_path)
    elif os.path.exists(xlsx_path):
        print(f"Loading {table_name} from Excel...")
        return pd.read_excel(xlsx_path)
    else:
        # Fallback check: look for files that *contain* the table name
        for file in os.listdir(folder_path):
            if table_name.lower() in file.lower():
                full_path = os.path.join(folder_path, file)
                if file.endswith('.csv'):
                    return pd.read_csv(full_path)
                elif file.endswith(('.xlsx', '.xls')):
                    return pd.read_excel(full_path)
        raise FileNotFoundError(f"Could not find data file for table: {table_name}")

def main():
    # Path where the folder will sit relative to your execution path
    data_folder = "./data/DE Dataset - intern"
    
    if not os.path.exists(data_folder):
        print(f"Error: Data folder not found at {data_folder}. Please place the folder there.")
        return

    try:
        # 1. Load tables
        user_logs = load_table(data_folder, "user_logs")
        user_referrals = load_table(data_folder, "user_referrals")
        
        print("\n--- Data Profiling Summary ---")
        print(f"User Logs Shape: {user_logs.shape}")
        print(f"User Referrals Shape: {user_referrals.shape}")
        
        # 2. Basic Fraud Detection Logic Example:
        # Flagging if multiple referred users share the exact same IP address
        print("\nChecking for potential fraud...")
        if 'ip_address' in user_logs.columns and 'referred_user_id' in user_referrals.columns:
            # Simple aggregation to find duplicate IPs
            suspicious_ips = user_logs['ip_address'].value_counts()
            suspicious_ips = suspicious_ips[suspicious_ips > 3] # Flagging more than 3 accounts on 1 IP
            print(f"Found {len(suspicious_ips)} IP addresses with high registration velocity.")
            
        # 3. Save Output Report
        os.makedirs("./output", exist_ok=True)
        user_logs.head(100).to_csv("./output/fraud_profile_report.csv", index=False)
        print("\nPipeline completed! Report saved to ./output/fraud_profile_report.csv")
        
    except Exception as e:
        print(f"An error occurred during pipeline execution: {e}")

if __name__ == "__main__":
    main()
