import streamlit as st

st.set_page_config(page_title="Caregiver Routine & Activity Planner", page_icon="🎨", layout="centered")

st.title("🎨 The Mindful Caregiver: Smart Routine & Activity Builder")
st.markdown("An interactive planning tool designed to balance daily routines, creative play, and structured learning for children based on age and energy levels.")

st.sidebar.header("Daily Context")
child_age = st.sidebar.selectbox("Child's Age Group", ["Toddler (1-3 yrs)", "Preschool (4-5 yrs)", "School-Age (6-9 yrs)"])
energy_level = st.sidebar.selectbox("Current Energy Level", ["Low / Overtired (Needs Quiet/Calm)", "Balanced & Focused", "High Energy (Needs to Burn Steam)"])
focus_area = st.sidebar.selectbox("Primary Goal for the Block", ["Creative Arts & Crafts", "Physical Activity & Motor Skills", "Cognitive & Logic Play"])

st.divider()
st.subheader("📋 Generated Daily Plan & Recommendations")

if energy_level == "Low / Overtired (Needs Quiet/Calm)":
    activity = "Guided storytelling, quiet acrylic/water painting exploration, or looking through a picture book."
    tip = "Keep transitions slow and low-stakes. Focus on sensory grounding."
elif energy_level == "High Energy (Needs to Burn Steam)":
    if child_age == "Toddler (1-3 yrs)":
        activity = "Indoor obstacle course using cushions, balancing games, and active stretching."
        tip = "Channel that energy into gross motor movement before trying any seated focus work."
    else:
        activity = "Outdoor bike/rollerblade escort, active park scavenger hunt, or dynamic movement games."
        tip = "Great window for physical coordination and burning off cortisol."
else:  
    if focus_area == "Creative Arts & Crafts":
        activity = "Self-portrait sketching, color mixing experimentation, or illustrating a short story together."
        tip = "Ask open-ended questions about their artwork ('Tell me about this color choice?') rather than steering the design."
    elif focus_area == "Cognitive & Logic Play":
        activity = "Pattern matching, sorting games, or building narrative logic sequences."
        tip = "Keep it playful and collaborative—let them lead the logic."
    else:
        activity = "A structured mix of independent play followed by a guided cooperative game."
        tip = "Encourage self-reliance during the independent phase."

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Selected Age Group", value=child_age)
with col2:
    st.metric(label="Energy State", value=energy_level)

st.markdown("### ✨ Recommended Activity:")
st.success(activity)

st.markdown("### 💡 Caregiver Pro-Tip:")
st.info(tip)

st.divider()
st.caption("Built with Python & Streamlit — combining computer science logic with real-world professional childcare expertise.")
