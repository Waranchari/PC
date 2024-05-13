import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# Function to load inventory data
def load_data():
    # Load data from CSV file (replace 'inventory.csv' with your file path)
    data = pd.read_csv('inventory.csv')
    return data

# Function to save inventory data
def save_data(data):
    # Save data to CSV file (replace 'inventory.csv' with your file path)
    data.to_csv('inventory.csv', index=False)

# Function to create dashboard
def create_dashboard(data):
    st.title('แดชบอร์ดสินค้า')

    # Group by category and calculate total quantity
    category_data = data.groupby('หมวดงาน')['จำนวนที่รับเข้า'].sum().reset_index()

    # Plot bar chart
    st.subheader('จำนวนทั้งหมดตามหมวดหมู่')
    fig, ax = plt.subplots()

    # Set default font family to a font that supports Thai characters
    plt.rcParams['font.family'] = 'Tahoma'

    sns.barplot(x='หมวดงาน', y='จำนวนที่รับเข้า', data=category_data, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Main function to run the app
def main():
    # Load inventory data
    data = load_data()

    # Set up sidebar
    st.sidebar.title('การจัดการสินค้า')
    page = st.sidebar.radio('การนำทาง', ['ดูสินค้า', 'เพิ่มสินค้า', 'แดชบอร์ด'])

    # View Inventory page
    if page == 'ดูสินค้า':
        st.title('ดูสินค้า')

        # Filter items by category
        categories = data['หมวดงาน'].unique().tolist()
        selected_category = st.selectbox('เลือกหมวดหมู่', ['ทั้งหมด'] + categories)
        
        if selected_category != 'ทั้งหมด':
            filtered_data = data[data['หมวดงาน'] == selected_category]
        else:
            filtered_data = data

        st.write(filtered_data)

    # Add Item page
    elif page == 'เพิ่มสินค้า':
        st.title('เพิ่มสินค้า')
        # Get user input for new item details
        name = st.text_input('ชื่อสินค้า')
        quantity = st.number_input('จำนวน', min_value=0)
        price = st.number_input('ราคา', min_value=0.0)

        # Add button to add item to inventory
        if st.button('เพิ่มสินค้า'):
            # Append new item to data
            new_item = {'ชื่อสินค้า': name, 'จำนวน': quantity, 'ราคา': price}
            data = data.append(new_item, ignore_index=True)
            # Save data
            save_data(data)
            st.success('เพิ่มสินค้าเรียบร้อยแล้ว!')

    # Dashboard page
    elif page == 'แดชบอร์ด':
        create_dashboard(data)

if __name__ == '__main__':
    main()
