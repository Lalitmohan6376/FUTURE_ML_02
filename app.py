import streamlit as st
import joblib

model = joblib.load("ticket_model.pkl")

st.set_page_config(page_title="Ticket Classifier", page_icon="🎫", layout="centered")

priority_map = {
    "Hardware": "High",
    "Access": "High",
    "Storage": "Medium",
    "HR Support": "Low",
    "Purchase": "Low",
    "Internal Project": "Medium",
    "Miscellaneous": "Low"
}

st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}
h1 {
    color: #38bdf8;
    text-align: center;
    font-size: 42px;
}
h3 {
    color: #e2e8f0;
}
.stTextArea textarea {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
    border: 1px solid #38bdf8;
    padding: 12px;
    font-size: 16px;
}
.stButton>button {
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    border: none;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #0ea5e9, #4f46e5);
}
.result-box {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #38bdf8;
    text-align: center;
    font-size: 22px;
    color: #22c55e;
    font-weight: bold;
}
.info-box {
    background: #020617;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #38bdf8;
    color: #cbd5f5;
}
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎫 Ticket Classification System</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
This intelligent system analyzes your support ticket and predicts the most relevant category using Machine Learning.
It also assigns a priority level to help support teams respond faster and smarter.
Enter your issue below and get instant results.
</div>
""", unsafe_allow_html=True)

st.markdown("<h3>📝 Enter Your Issue</h3>", unsafe_allow_html=True)

user_input = st.text_area("", height=180, placeholder="Describe your issue here...")

if st.button("🚀 Predict Category"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text first")
    else:
        prediction = model.predict([user_input])[0]
        priority = priority_map.get(prediction, "Medium")

        st.markdown("<h3>📊 Prediction Result</h3>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-box">
        📂 Category: {prediction} <br><br>
        ⚡ Priority: {priority}
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
Made with ❤️ using Streamlit | Machine Learning Project
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#020617;padding:20px;border-radius:12px;border-left:6px solid #38bdf8;margin-bottom:20px;">

<h3 style="color:#38bdf8;">📝 How to Write a Good Ticket Description</h3>

<ul style="color:#cbd5f5;font-size:16px;line-height:1.8;">
<li>✔ Write your issue in a <b>clear and simple way</b></li>
<li>✔ Mention the <b>type of problem</b> (system, login, salary, storage, etc.)</li>
<li>✔ Use <b>specific keywords</b> like “login issue”, “disk full”, “salary issue”</li>
<li>✔ Avoid vague sentences like <i>“something is wrong”</i></li>
<li>✔ Explain <b>what you were doing</b> when the issue happened</li>
<li>✔ Keep it <b>short but meaningful</b></li>
<li>✔ Write <b>only one issue at a time</b></li>
</ul>

<hr style="border:1px solid #1e293b;">

<p style="color:#94a3b8;">
❌ Example: I have some issue <br>
✅ Example: I am unable to login to my system and it shows access denied error
</p>

<p style="color:#22c55e;font-weight:bold;">
💡 Better descriptions = More accurate predictions
</p>

</div>
""", unsafe_allow_html=True)