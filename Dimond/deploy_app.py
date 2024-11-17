

# Install dependencies
import os
os.system('pip install -r "/content/hrushi-ml-model-deployment/requirements.txt"')
from threading import Thread
from pyngrok import ngrok

ngrok.set_auth_token('2ealQmcvdF5FBFeob5NlTJzoHOQ_7yix6hSXHXpcuR8wULd5t')

# Function to deploy and get the public URL of the app
def deploy_app():
    # Clone the repository
    os.system('git clone https://github.com/hrushi1402/hrushi-ml-model-deployment.git')
    os.system('pip install -r "/content/hrushi-ml-model-deployment/requirements.txt"')

    # Function to run the Streamlit app
    def run_streamlit():
        os.system('streamlit run /content/hrushi-ml-model-deployment/Dimond/app.py --server.port 8501')

    # Start a thread to run the Streamlit app
    thread = Thread(target=run_streamlit)
    thread.start()

    # Get the public URL for the app
    public_url = ngrok.connect(addr='8501', proto='http', bind_tls=True)
    print('Your Streamlit app is live at:', public_url)

# Call deploy_app function to deploy the app
deploy_app()
