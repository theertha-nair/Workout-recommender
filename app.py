import streamlit as st
import pandas as pd
from src.recommended import load_exercises, generate_plan
from src.progression import progress_plan

st.title("🏋️ Workout Recommender")

# Sidebar input
with st.sidebar:
    st.header("User Profile")
    level = st.selectbox("Level", ["beginner", "intermediate", "advanced"])
    goal = st.selectbox("Goal", ["muscle", "strength", "cardio"])
    equipment = st.multiselect("Equipment", ["bodyweight", "dumbbell", "barbell", "resistance_band"])
    days = st.slider("Days per week", 1, 6, 3)
    week = st.slider("Training Week", 1, 12, 1)
    submitted = st.button("Generate Plan")

if submitted:
    df = load_exercises("data\exercises.csv")
    user = {"level": level, "goal": goal, "equipment": equipment, "days": days}
    base_plan = generate_plan(user, df)
    plan = progress_plan(base_plan, week)

    for day, exs in plan.items():
        st.header(day)
        for ex in exs:
            # Display different formats depending on type
            if ex.get("type") == "reps" or ex.get("default_rep_unit") == "reps":
                st.markdown(f"**{ex['exercise']}** — {ex.get('progressed_sets', ex.get('default_sets', 3))} sets x {ex.get('progressed_reps', ex.get('base_reps', '?'))} reps")

            elif ex.get("type") == "time" or ex.get("default_rep_unit") == "seconds":
                st.markdown(f"**{ex['exercise']}** — {ex.get('progressed_sets', ex.get('default_sets', 3))} sets x {ex.get('progressed_time', ex.get('base_time', '?'))} sec")

            elif ex.get("type") == "weight" or ex.get("default_rep_unit") == "kg":
                st.markdown(f"**{ex['exercise']}** — {ex.get('progressed_sets', ex.get('default_sets', 3))} sets x {ex.get('progressed_reps', ex.get('base_reps', '?'))} reps @ {ex.get('progressed_weight', ex.get('base_weight', '?'))} kg")

            # Show equipment as caption
            st.caption(f"Equipment: {ex['equipment']}")