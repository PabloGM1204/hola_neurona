FROM python:3.10
RUN pip install streamlit
WORKDIR /app
# COPY src/* /app/
ENTRYPOINT [ "streamlit", "run", "streamlit_app.py" ]