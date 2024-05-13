import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

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

    # Plot bar chart using Plotly
    st.subheader('จำนวนทั้งหมดตามหมวดหมู่')
    fig = px.bar(category_data, x='หมวดงาน', y='จำนวนที่รับเข้า', title='จำนวนทั้งหมดตามหมวดหมู่')
    fig.update_layout(
        xaxis_title='หมวดงาน (Category)',
        yaxis_title='จำนวนที่รับเข้า (Total Quantity)',
        font=dict(
            family='Tahoma'
        )
    )
    fig.update_xaxes(tickangle=45)

    st.plotly_chart(fig)

def equipment_dashboard(data):  # Accept data as a parameter
    # Create a dashboard title
    st.title("ประวัติการรับเข้า")

    # Create a main content area
    with st.form("equipment_form"):
        # Create a section for equipment information
        st.header("ข้อมูลรับเข้า")
        equipment_name = st.selectbox("ชื่ออุปกรณ์", data['ชื่ออุปกรณ์'])
        quantity = st.number_input("จํานวน", value=0)
        received_by = st.text_input("ผู้รับเข้า")
        notes = st.text_area("หมายเหตุ")
        
        current_date = datetime.now().date()

        # Date input with default value set to current date
        date_received = st.date_input("วันที่รับเข้า", value=current_date)

        # Create a submit button
        submitted = st.form_submit_button("Submit")

        # Create a cancel button
        st.form_submit_button("Cancel")

    # Display a message if the form is submitted
    if submitted:
        st.write("Form submitted successfully!")

def create_dashboard_1(data):
    st.title("Inventory Dashboard")

    # Set custom font using CSS
    st.markdown(
        """
        <style>
        /* Define your custom font */
        .custom-font {
            font-family: 'TH Sarabun New', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display content with custom font
    st.write("This text uses a custom font.", unsafe_allow_html=True)


# Main function to run the app
def main():
    # Load inventory data
    data = load_data()
    create_dashboard_1(data)

    # Set up sidebar
    st.sidebar.title('การจัดการสินค้า')
    page = st.sidebar.radio('การนำทาง', ['ดูสินค้า', 'เพิ่มสินค้า', 'แดชบอร์ด','ประวัติการรับเข้า'])

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
        
    elif page == 'ประวัติการรับเข้า':
        equipment_dashboard(data)  # Pass data to equipment_dashboard function

if __name__ == '__main__':
    main()
