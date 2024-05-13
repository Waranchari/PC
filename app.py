import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv('inventory.csv')
    return data

def save_data(data):
    # Save data to CSV file (replace 'inventory.csv' with your file path)
    data.to_csv('inventory.csv', index=False)

def create_dashboard(data):
    st.title('Inventory Dashboard')

    # Group by category and calculate total quantity
    category_data = data.groupby('หมวดงาน')['จำนวนที่รับเข้า'].sum().reset_index()

    # Plot bar chart
    st.subheader('Total Quantity by Category')
    fig, ax = plt.subplots()
    sns.barplot(x='หมวดงาน', y='จำนวนรับเข้า', data=category_data, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Main function to run the app
def main():
    # Load inventory data
    data = load_data()

    # Set up sidebar
    st.sidebar.title('Inventory Management')
    page = st.sidebar.radio('Navigation', ['View Inventory', 'Add Item', 'Dashboard'])

    # View Inventory page
    if page == 'View Inventory':
        st.title('View Inventory')

        # Filter items by category
        categories = data['หมวดงาน'].unique().tolist()
        selected_category = st.selectbox('Select Category', ['All'] + categories)
        
        if selected_category != 'All':
            filtered_data = data[data['หมวดงาน'] == selected_category]
        else:
            filtered_data = data

        st.write(filtered_data)

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

    # Dashboard page
    elif page == 'Dashboard':
        create_dashboard(data)

if __name__ == '__main__':
    main()
