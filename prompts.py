"""
Email Prompt Builder using RCFC Framework
------------------------------------------
This module constructs structured prompts for generating professional emails.

RCFC Framework:
- Role: Define AI's persona
- Context: Provide background information
- Format: Specify output structure
- Constraints: Set limitations and requirements
"""

def build_email_prompt(
    sender_name: str,
    sender_role: str,
    recipient_name: str,
    recipient_role: str,
    purpose: str,
    context: str,
    tone: str,
    length: str,
    key_points: str
) -> str:
    """
    Builds a structured prompt for email generation using RCFC framework.
    
    Args:
        sender_name: Name of the email sender
        sender_role: Professional role/title of sender
        recipient_name: Name of the email recipient
        recipient_role: Professional role/title of recipient
        purpose: Main purpose/goal of the email
        context: Additional background information
        tone: Desired tone (Professional, Formal, Friendly, Persuasive)
        length: Target length (Short, Medium, Long)
        key_points: Important points to include (newline-separated)
    
    Returns:
        str: Complete structured prompt ready for LLM
    """
    
    # Parse length constraint
    word_limit_map = {
        "Short (< 100 words)": "under 100 words",
        "Medium (100-200 words)": "between 100-200 words",
        "Long (200-300 words)": "between 200-300 words"
    }
    word_limit = word_limit_map.get(length, "around 150 words")
    
    # Build prompt using RCFC framework
    prompt = f"""Role: You are a professional email writing assistant specializing in academic and business communication.

Context:
- Sender: {sender_name}, {sender_role}
- Recipient: {recipient_name}, {recipient_role}
- Purpose: {purpose}"""
    
    # Add optional context if provided
    if context and context.strip():
        prompt += f"\n- Background: {context.strip()}"
    
    prompt += f"""

Task: Write a complete professional email for the above situation.

Format Requirements:
- Start with subject line (format: "Subject: [your subject]")
- Include appropriate greeting (e.g., "Dear Dr. Smith," or "Hi John,")
- Write clear, well-structured body paragraphs
- End with professional closing (e.g., "Best regards," "Sincerely,")
- Include sender's signature block

Constraints:
- Tone: {tone}
- Length: {word_limit}
- Use proper email etiquette and formatting"""
    
    # Add key points if provided
    if key_points and key_points.strip():
        prompt += f"\n- Must naturally incorporate these points:\n{key_points.strip()}"
    
    prompt += """

Output the complete email ready to copy and send. Do not include any explanations or meta-commentary outside the email itself.
"""
    
    return prompt


def get_email_templates():
    """
    Returns a dictionary of pre-configured email templates for common scenarios.
    
    Returns:
        dict: Template name -> template configuration
    """
    templates = {
        "Custom": {
            "purpose": "",
            "context": "",
            "key_points": "",
            "tone": "Professional"
        },
        
        "Research Assistantship": {
            "purpose": "Express interest in joining your research team as a Research Assistant",
            "context": "I am a graduate student with relevant coursework and research experience",
            "key_points": """- My research interests align with your work
- Completed relevant coursework (Machine Learning, Data Analytics)
- Technical skills in Python, R, and data analysis
- Request for meeting to discuss opportunities""",
            "tone": "Professional"
        },
        
        "Networking / Informational Interview": {
            "purpose": "Request a brief informational interview to learn about your career path",
            "context": "I came across your profile and am impressed by your work in the field",
            "key_points": """- Admire their career trajectory and accomplishments
- Currently exploring career options in the field
- Request 15-20 minute virtual coffee chat
- Flexible with their schedule""",
            "tone": "Friendly"
        },
        
        "Thank You (After Meeting)": {
            "purpose": "Thank you for taking the time to meet with me",
            "context": "Following up after our recent conversation",
            "key_points": """- Express genuine gratitude for their time
- Mention specific insight or advice that resonated
- Reiterate interest in staying connected
- Offer to reciprocate or provide value""",
            "tone": "Friendly"
        },
        
        "Follow-Up (No Response)": {
            "purpose": "Following up on my previous email from [date]",
            "context": "I reached out last week regarding [topic] but haven't heard back",
            "key_points": """- Gentle reminder about previous email
- Acknowledge they may be busy
- Briefly restate the request or purpose
- Offer alternative timing or format""",
            "tone": "Professional"
        },
        
        "Project Collaboration Request": {
            "purpose": "Propose a potential collaboration on [project topic]",
            "context": "I have an idea that aligns with both our interests and expertise",
            "key_points": """- Brief description of the project idea
- Why this collaboration makes sense
- What you bring to the table
- Suggest next steps (meeting, call)""",
            "tone": "Persuasive"
        }
    }
    
    return templates


# Tone guidelines for reference
TONE_DESCRIPTIONS = {
    "Professional": "Respectful, clear, business-appropriate. Balanced formality.",
    "Formal": "Very polite, traditional language. Conservative and deferential.",
    "Friendly": "Warm, personable, conversational. Still respectful but more casual.",
    "Persuasive": "Confident, action-oriented, compelling. Emphasizes benefits and value."
}