import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv('inventory.csv')
    return data

def save_data(data):
    # Save data to CSV file (replace 'inventory.csv' with your file path)
    data.to_csv('inventory.csv', index=False)

# Main function to run the app
def main():
    # Load inventory data
    data = load_data()

    # Set up sidebar
    st.sidebar.title('Inventory Management')
    page = st.sidebar.radio('Navigation', ['View Inventory', 'Add Item'])

    # View Inventory page
    if page == 'View Inventory':
        st.title('View Inventory')
        st.write(data)

    # Add Item page
    elif page == 'Add Item':
        st.title('Add Item')
        # Get user input for new item details
        name = st.text_input('Name')
        quantity = st.number_input('Quantity', min_value=0)
        price = st.number_input('Price', min_value=0.0)

        # Add button to add item to inventory
        if st.button('Add Item'):
            # Append new item to data
            new_item = {'Name': name, 'Quantity': quantity, 'Price': price}
            data = data.append(new_item, ignore_index=True)
            # Save data
            save_data(data)
            st.success('Item added successfully!')


# Load data
equipment_data = pd.read_csv('inventory.csv.csv')

# Create title
st.title('Equipment Inventory Dashboard')

# Display data
st.subheader('Equipment in Stock')
st.dataframe(equipment_data[['ชื่ออุปกรณ์', 'จำนวนที่รับเข้า']])

# Display received and issued data
st.subheader('Received and Issued Equipment')
received_data = equipment_data[equipment_data['Transaction Type'] == 'Received']
issued_data = equipment_data[equipment_data['Transaction Type'] == 'Issued']

st.write('Received Equipment:')
st.dataframe(received_data[['Equipment Name', 'Quantity']])
st.write('Issued Equipment:')
st.dataframe(issued_data[['Equipment Name', 'Quantity']])

# Display monthly chart
st.subheader('Monthly Equipment Inflow and Outflow')
monthly_data = equipment_data.groupby(['Transaction Date', 'Transaction Type']).sum().reset_index()
monthly_data['Month'] = monthly_data['Transaction Date'].dt.month
monthly_chart = monthly_data.pivot(index='Month', columns='Transaction Type', values='Quantity').fillna(0)
st.bar_chart(monthly_chart)

# Add interactivity
equipment_name = st.selectbox('Select Equipment', equipment_data['Equipment Name'])
received_data_filtered = received_data[received_data['Equipment Name'] == equipment_name]
issued_data_filtered = issued_data[issued_data['Equipment Name'] == equipment_name]

st.subheader('Filtered Equipment Data')
st.write('Received Equipment:')
st.dataframe(received_data_filtered[['Transaction Date', 'Quantity']])
st.write('Issued Equipment:')
st.dataframe(issued_data_filtered[['Transaction Date', 'Quantity']])
if __name__ == '__main__':
    main()
