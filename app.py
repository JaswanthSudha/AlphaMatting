import streamlit as st 
from PIL import Image 
from rembg import remove 
def main():
    st.title("Background Remover")
    uploaded_img=st.file_uploader(label="upload and image",type=[
        "png","jpg","jpeg"
    ],accept_multiple_files=False)
    if st.button("Generate"):
        if uploaded_img:
            try:
                img=Image.open(uploaded_img)
                res_img=remove(img)
                st.toast("AI completed work",icon="🎊")
                # Creating two columns
                col1,col2=st.columns(2,gap="large")
                with col1:
                    st.markdown("## Original Image")
                    st.image(uploaded_img)
                with col2:
                    st.markdown("## Final Image")
                    st.image(res_img)
            except:
                st.error("Unable to read image - File may be corrupted")
        else:
            st.warning("Please upload an image")
        
if __name__ == "__main__":
    main()