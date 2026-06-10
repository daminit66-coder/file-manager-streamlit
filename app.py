import streamlit as st
from pathlib import Path

st.set_page_config(page_title="File Manager", page_icon="📁", layout="centered")

st.title("📁 File Manager App")
st.write("A simple Python file handling project with Streamlit UI")

menu = st.sidebar.selectbox(
    "Choose Operation",
    ["Read File", "Create File", "Update File", "Delete File"]
)

# ---------------- READ FILE ----------------
if menu == "Read File":
    st.header("📖 Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read"):
        path = Path(file_name)

        if path.exists():
            content = path.read_text(encoding="utf-8")
            st.success("File Read Successfully!")
            st.text_area("File Content", content, height=300)
        else:
            st.error("File not found!")

# ---------------- CREATE FILE ----------------
elif menu == "Create File":
    st.header("✍️ Create File")

    file_name = st.text_input("Enter new file name")
    content = st.text_area("Enter content")

    if st.button("Create"):
        path = Path(file_name)

        if path.exists():
            st.error("File already exists!")
        else:
            path.write_text(content, encoding="utf-8")
            st.success("File created successfully!")

# ---------------- UPDATE FILE ----------------
elif menu == "Update File":
    st.header("🔄 Update File")

    file_name = st.text_input("Enter file name")

    if Path(file_name).exists():
        option = st.radio(
            "Choose update option",
            ["Append", "Overwrite", "Rename"]
        )

        if option == "Append":
            new_text = st.text_area("Text to append")

            if st.button("Append"):
                with open(file_name, "a", encoding="utf-8") as f:
                    f.write("\n" + new_text)
                st.success("Content appended!")

        elif option == "Overwrite":
            new_text = st.text_area("New content")

            if st.button("Overwrite"):
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(new_text)
                st.success("File overwritten!")

        elif option == "Rename":
            new_name = st.text_input("New file name")

            if st.button("Rename"):
                Path(file_name).rename(new_name)
                st.success("File renamed successfully!")

    else:
        st.warning("Enter a valid existing file name")

# ---------------- DELETE FILE ----------------
elif menu == "Delete File":
    st.header("🗑️ Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete"):
        path = Path(file_name)

        if path.exists():
            path.unlink()
            st.success("File deleted successfully!")
        else:
            st.error("File not found!")