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

    # Show footer
    st.sidebar.markdown('---')
    st.sidebar.write('Built with Streamlit')

if __name__ == '__main__':
    main()
