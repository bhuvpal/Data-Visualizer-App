import os


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st
st.set_page_config("Data Visualizer",layout="centered",page_icon="📊")
st.title("📊Data Visualizer Web App")



working_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = f"{working_dir}/data"


files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]


selected_file = st.selectbox("Select a file", files_list,index=None)

if selected_file:
      file_path = os.path.join(folder_path, selected_file)
      df = pd.read_csv(file_path)

      col1,col2 = st.columns(2)
      column = df.columns.tolist()

      with col1:
        st.subheader("Data preview")
        st.dataframe(df.head())

      with (col2):
           x_axis = st.selectbox("Select x-axis", column+["None"],index=len(column))
           y_axis = st.selectbox("Select y-axis", column+["None"],index=len(column))
           plot_type = ["Count Plot","Bar Plot","Line Plot","Scatter Plot","Box Plot","Histogram","Pie Chart","Distribution plot"]
           selected_plot_type = st.selectbox("Select plot type", plot_type+["None"])
           if selected_plot_type == "Count Plot":
              if x_axis == "None" and y_axis == "None":
                 st.error("Please select An-axis")
              else:
                  if st.button("Show Count Plot"):
                     st.subheader("Count Plot")
                     fig = plt.figure(figsize=(20,10))
                     sns.countplot(x=x_axis,data=df,hue=x_axis,legend=False)
                     st.pyplot(fig)

           elif selected_plot_type == "Bar Plot":
                if x_axis == "None" and y_axis == "None":
                   st.error("Please select x-axis")
                else:
                     if st.button("Show Bar Plot"):
                        st.subheader("Bar Plot")
                        fig = plt.figure(figsize=(10, 6))
                        sns.barplot(x=x_axis,y=y_axis,data=df,hue=x_axis,legend=False)
                        st.pyplot(fig)

           elif selected_plot_type == "Line Plot":
                if x_axis == "None" or y_axis == "None":
                   st.error("Please select both axis X-Axis and Y-Axis")
                else:
                    st.subheader("Line Plot")
                    fig = plt.figure(figsize=(10, 6))
                    sns.lineplot(x=x_axis,y=y_axis,data=df)
                    st.pyplot(fig)
           elif selected_plot_type == "Scatter Plot":
                if x_axis == "None" and y_axis == "None":
                   st.error("Please select x-axis")
                else:
                     if st.button("Show Scatter Plot"):
                        st.subheader("Scatter Plot")
                        fig = plt.figure(figsize=(10, 6))
                        sns.scatterplot(x=df[x_axis],y=df[y_axis],data=df)
                        st.pyplot(fig)
           elif selected_plot_type == "Box Plot":
                if x_axis == "None":
                   st.error("Please select x-axis")
                else:
                     if st.button("Show Box Plot"):
                        st.subheader("Box Plot")
                        fig = plt.figure(figsize=(10, 6))
                        sns.boxplot(x=x_axis,data=df)
                        st.pyplot(fig)
           elif selected_plot_type == "Histogram":
                if x_axis == "None":
                   st.error("Please select x-axis")
                else:
                     if st.button("Show Histogram"):
                        st.subheader("Histogram")
                        fig = plt.figure(figsize=(20, 10))
                        sns.histplot(x=x_axis,kde=True,data=df)
                        st.pyplot(fig)
           elif selected_plot_type == "Pie Chart":
               if x_axis == "None":
                   st.error("Please select x-axis categorical feature")
               else:
                   if st.button("Show Pie Chart"):
                       st.subheader("Pie Chart")
                       fig = plt.figure(figsize=(10, 6))
                       plt.pie(df[x_axis].value_counts(),labels=df[x_axis].value_counts().index,autopct="%1.1f%%",shadow=True)
                       st.pyplot(fig)
           elif selected_plot_type == "Distribution plot":
                if x_axis == "None":
                   st.error("Please select x-axis")
                else:
                     if st.button("Show Distribution plot"):
                        st.subheader("Distribution Plot")
                        fig = plt.figure(figsize=(20, 10))
                        sns.distplot(x=df[x_axis])
                        st.pyplot(fig)







