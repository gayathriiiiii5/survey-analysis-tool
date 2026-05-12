import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from analysis import process_data, get_summary

# IMPORTANT: must be first Streamlit command
st.set_page_config(page_title="Survey Analysis Tool", layout="wide")

st.title("Automated Survey Analysis Tool")

# File upload
file = st.file_uploader("Upload your survey CSV", type=["csv"])

if file is not None:
    # Read CSV once
    df = pd.read_csv(file) 
    print(df.columns)

    st.subheader("Raw Data")
    st.dataframe(df)

    # Process data
    df = process_data(df)

    st.subheader("Processed Data")
    st.dataframe(df)

    # Summary
    summary = get_summary(df)

    st.subheader("Key Insights")
    st.write(summary)

    # Sentiment Chart (safe check)
    if "Sentiment" in df.columns:
        st.subheader("Sentiment Distribution")
        fig, ax = plt.subplots()
        df["Sentiment"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No 'Sentiment' column found in dataset.")

    # Rating Chart (safe check)
    if "Rating" in df.columns:
        st.subheader("Rating Distribution")
        fig2, ax2 = plt.subplots()
        df["Rating"].hist(ax=ax2)
        st.pyplot(fig2)
    else:
        st.warning("No 'Rating' column found in dataset.")

    # Download processed file
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Processed Data",
        data=csv,
        file_name="results.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a CSV file to begin.")