from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title("Inventory Management")

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("example_app/streamlit_app.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("example_app/example_one.py", "Example One", ":books:"),
        # The pages appear in the order you pass them
        Page("example_app/example_four.py", "Example Four", "📖"),
        Page("example_app/example_two.py", "Example Two", "✏️"),
        # Will use the default icon and name based on the filename if you don't
        # pass them
        Page("example_app/example_three.py"),
        Page("example_app/example_five.py", "Example Five", "🧰"),
    ]
)
