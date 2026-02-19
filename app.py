"""
Professional Email Generator
-----------------------------
Using Google Gemini (Free tier with better limits!)
"""

import streamlit as st

# MUST BE FIRST
st.set_page_config(
    page_title="Professional Email Generator",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import build_email_prompt, get_email_templates, TONE_DESCRIPTIONS

# Load environment variables
load_dotenv()

# Configure Gemini
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        client_ready = True
    else:
        client_ready = False
        error_msg = "GEMINI_API_KEY not found in .env"
except Exception as e:
    client_ready = False
    error_msg = str(e)


def generate_email(prompt, temperature=0.7):
    """Generate email using Google Gemini"""
    if not client_ready:
        raise Exception("Gemini client not initialized")
    
    try:
        # Configure generation parameters
        generation_config = {
            "temperature": temperature,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 1024,
        }
        
        # Generate response
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        return response.text.strip()
    
    except Exception as e:
        raise e


def main():
    """Main application function"""
    
    # Check API key
    if not client_ready:
        st.error("⚠️ Google Gemini API key not found or invalid")
        st.info("""
        **How to get a free Gemini API key:**
        1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
        2. Click "Get API Key"
        3. Create a new project or use existing
        4. Copy the API key
        5. Add to `.env` file: `GEMINI_API_KEY=your_key_here`
        """)
        st.warning("**Note:** Gemini has MUCH better free tier limits than OpenAI!")
        st.stop()
    
    # Header
    st.markdown('<p style="font-size:2.5rem; font-weight:700; color:#1f77b4;">✉️ Professional Email Generator</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.2rem; color:#666;">Powered by Google Gemini (Free & Fast!)</p>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.header("📝 Email Details")
    
    # Template selector
    st.sidebar.subheader("Quick Start")
    templates = get_email_templates()
    selected_template = st.sidebar.selectbox(
        "Choose a template:",
        list(templates.keys()),
        help="Select a pre-configured template"
    )
    
    template_data = templates[selected_template]
    
    st.sidebar.divider()
    
    # Sender
    st.sidebar.subheader("From (You)")
    sender_name = st.sidebar.text_input(
        "Your Name",
        placeholder="e.g., John Doe"
    )
    sender_role = st.sidebar.text_input(
        "Your Role",
        placeholder="e.g., Graduate Student"
    )
    
    st.sidebar.divider()
    
    # Recipient
    st.sidebar.subheader("To (Recipient)")
    recipient_name = st.sidebar.text_input(
        "Recipient Name",
        placeholder="e.g., Dr. Jane Smith"
    )
    recipient_role = st.sidebar.text_input(
        "Recipient Role",
        placeholder="e.g., Professor"
    )
    
    st.sidebar.divider()
    
    # Content
    st.sidebar.subheader("Content")
    purpose = st.sidebar.text_area(
        "Purpose of Email",
        value=template_data["purpose"],
        height=80,
        placeholder="What is this email about?"
    )
    
    context = st.sidebar.text_area(
        "Background/Context (Optional)",
        value=template_data.get("context", ""),
        height=100,
        placeholder="Any relevant background..."
    )
    
    key_points = st.sidebar.text_area(
        "Key Points to Include",
        value=template_data.get("key_points", ""),
        height=120,
        placeholder="- Point 1\n- Point 2"
    )
    
    st.sidebar.divider()
    
    # Style
    st.sidebar.subheader("Style & Format")
    tone = st.sidebar.selectbox(
        "Tone",
        ["Professional", "Formal", "Friendly", "Persuasive"],
        index=["Professional", "Formal", "Friendly", "Persuasive"].index(
            template_data.get("tone", "Professional")
        )
    )
    st.sidebar.caption(f"💡 {TONE_DESCRIPTIONS[tone]}")
    
    length = st.sidebar.selectbox(
        "Length",
        ["Short (< 100 words)", "Medium (100-200 words)", "Long (200-300 words)"],
        index=1
    )
    
    st.sidebar.divider()
    
    # Buttons
    generate_button = st.sidebar.button(
        "✨ Generate Email",
        type="primary",
        use_container_width=True
    )
    
    if "generated_email" in st.session_state:
        regenerate_button = st.sidebar.button(
            "🔄 Regenerate (Different Version)",
            use_container_width=True
        )
    else:
        regenerate_button = False
    
    # Main area
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("📧 Generated Email")
        
        if generate_button or regenerate_button:
            # Validate
            if not all([sender_name, sender_role, recipient_name, recipient_role, purpose]):
                st.error("⚠️ Please fill in all required fields")
                st.stop()
            
            # Generate
            with st.spinner("✍️ Gemini is crafting your email..."):
                try:
                    # Build prompt
                    prompt = build_email_prompt(
                        sender_name=sender_name,
                        sender_role=sender_role,
                        recipient_name=recipient_name,
                        recipient_role=recipient_role,
                        purpose=purpose,
                        context=context,
                        tone=tone,
                        length=length,
                        key_points=key_points
                    )
                    
                    # Generate
                    temperature = 0.9 if regenerate_button else 0.7
                    email = generate_email(prompt, temperature)
                    
                    # Store
                    st.session_state.generated_email = email
                    st.session_state.last_prompt = prompt
                    
                    st.success("✅ Email generated successfully!")
                    
                except Exception as e:
                    error_msg = str(e).lower()
                    
                    if "api key" in error_msg or "authentication" in error_msg:
                        st.error("❌ Invalid API key. Check your .env file.")
                    elif "quota" in error_msg or "rate limit" in error_msg:
                        st.error("❌ Rate limit reached. Wait a moment and try again.")
                    elif "safety" in error_msg or "blocked" in error_msg:
                        st.warning("⚠️ Content was blocked by safety filters. Try rephrasing.")
                    else:
                        st.error(f"❌ Error: {str(e)}")
                    st.stop()
        
        # Display
        if "generated_email" in st.session_state:
            st.text_area(
                "Your Email:",
                value=st.session_state.generated_email,
                height=400,
                label_visibility="collapsed"
            )
            st.caption("💡 Select all and copy (Ctrl+A, Ctrl+C)")
        else:
            st.info("👈 Fill out the form and click 'Generate Email'")
            
            with st.expander("📖 Example"):
                st.markdown("""
                **Input:**
                - From: Sarah Chen, Graduate Student
                - To: Dr. Zhang, Professor  
                - Purpose: Express interest in research position
                
                **Output:** Polished professional email
                """)
    
    with col2:
        st.subheader("📊 Prompt Engineering")
        
        if "last_prompt" in st.session_state:
            with st.expander("🔍 See the AI Prompt", expanded=False):
                st.caption("Structured prompt sent to Gemini:")
                st.code(st.session_state.last_prompt, language="text")
                
                st.markdown("""
                **RCFC Framework:**
                - **R**ole: Email assistant
                - **C**ontext: Details provided
                - **F**ormat: Subject, greeting, body, closing
                - **C**onstraints: Tone, length, points
                """)
        
        st.subheader("💡 Tips")
        st.markdown("""
        **Best practices:**
        - ✅ Be specific about purpose
        - ✅ Include relevant context
        - ✅ List key points
        - ✅ Choose appropriate tone
        - ✅ Review before sending
        """)
        
        # Stats
        if "email_count" not in st.session_state:
            st.session_state.email_count = 0
        if generate_button:
            st.session_state.email_count += 1
        
        st.divider()
        st.metric("Emails Generated", st.session_state.email_count)
        
        # Info box
        st.info("""
        **Why Gemini?**
        - 🆓 Free tier: 60 requests/min
        - ⚡ Fast response times
        - 🎯 High quality outputs
        - 💰 No credit card needed
        """)


# Footer
st.divider()
st.caption("Built at AI Integration Bootcamp | Session 3 | Powered by Google Gemini")


if __name__ == "__main__":
    main()
    