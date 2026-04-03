import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="Gerador de QRCode")
st.title("Gerador de QRCode BorgesN")
st.markdown("Insira um texto, URL ou código para transformar em QRCode")

texto = st.text_input("Conteúdo do QRCode: ",placeholder="Exemplo: 'https://www.google.com.br")

if st.button("Gerar QRCode"):
    if texto.strip() == "":
        st.warning("O campo não pode estar vazio")
    else:
        qr = qrcode.QRCode(
            version=1,
            error_correction= qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black",back_color="white")

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        st.image(buf, caption="Seu QRCode está pronto",use_column_width=False)

        st.download_button(
            label="📥 Baixar QRCode",
            data=buf,
            file_name="QRCode.png",
            mime="image/png",
        )