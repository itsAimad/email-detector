import streamlit as st
import joblib


# load the model and Vectorizer

model = joblib.load(r"Email Detector\model\spam_classifier.pkl")
cv = joblib.load(r"Email Detector\model\count_vectorizer.pkl")


def predict_user_mail(mail,cv=cv,model=model):
    if not mail.strip():
        return "Please enter a valid email."
    
    email_count = cv.transform([mail])

    prediction = model.predict(email_count)

    return "This email is a spam" if prediction[0]==1 else "This email is not a spam"






st.markdown("<h1 style='text-align:center;' class=\"title\">Hello, This is a Spam Detector</h1>",unsafe_allow_html=True)
st.markdown("""<style>

            .stTextArea textarea:focus{
                box-shadow: 0px 0px 40px red;
                
             }

            .stButton>button{
                color:#fff;
                background-color:tranparent;
            }
            .stButton>button:hover{
                color: #4ca1af;
                border-color: #4ca1af;
            }
            .stButton>button:active{
                    color:#fff;
                    background-color:#4ca1af;
                }

           

            h1{
                color:#2c3e50;
                margin-bottom:10px;

                transition : 1s ease-out;
            }
            h1:hover{
                color:#4ca1af;

                transform: scale(1.1);
                }

            .container{
            display:flex;
            justify-content:center;
            align-items: center;
            width:100%;
            height:300px;
            

            }

            .result{
                display:flex;
                justify-content:center;
                align-items: center;
                border-radius : 26px;
                width:600px;
                height:300px;
                margin-top:10px;
                background: linear-gradient(to right,#2c3e50,#4ca1af);
                transition: 1s ease-in-out;
            }
            .result:hover{
                transform: scale(1.1);
                cursor:pointer;
                box-shadow:0px 0px 25px #fff;
            }

            .answer{
                font-size: 30px;
                
                position:relative;
                left: 92px;
                bottom : 7rem;
                font-weight: 600;
 
                }
            
            .predict{
                text-align:center;
                position:relative;
                right: 80px;
                font-size:20px;
            }
            .result:hover > .answer{
                border-bottom: 4px solid #fff;
                border-radius:10px;
                transition-duration:0.6s;
            }
            
            
            
    </style>""",unsafe_allow_html=True)

email=  st.text_area("Enter your message here: ")
if  len(email) ==0:
   
    st.markdown("""
          <style>
                .container{
                    display:none;
                }
                </style>
""",unsafe_allow_html=True)
    # st.markdown("YOU NEED TO ENTER AN EMAIL !!")
    

if st.button("Click"):
     if email.strip():
        result = predict_user_mail(email,cv,model)  
        st.markdown(
          f""" 
            <div class="container"> 
                <div class="result"> 
                    <p class="answer">The result is :  </p> 
                    <p class="predict">{result}</p> 
                </div> 
            </div> 
            """, unsafe_allow_html=True)
     else:
         st.warning("Please enter a valid email!")
