import streamlit as st

# Title of the app
st.title("Data Warehousing & Enterprise Data Management")

# Sidebar filters and options
st.sidebar.title("Data Management Topics")
topic_option = st.sidebar.selectbox(
    "Choose a topic to explore:", 
    ["Introduction", "ETL Process", "Data Models", "Data Governance"]
)

# Section 1: Introduction
if topic_option == "Introduction":
    st.header("What is Data Warehousing?")
    st.write("""
    A **Data Warehouse** (DW) is a system used for reporting and data analysis.
    It is a central repository of integrated data from one or more disparate sources.
    Data warehousing is used to store historical data for business intelligence purposes.
    """)

    st.write("""
    **Enterprise Data Management (EDM)** refers to the governance and management of data 
    across an entire enterprise, ensuring data is consistent, accessible, and accurate.
    """)

# Section 2: ETL Process
elif topic_option == "ETL Process":
    st.header("ETL Process in Data Warehousing")
    st.write("""
    The **ETL process** (Extract, Transform, Load) is essential in data warehousing. It involves:
    1. **Extracting** data from different sources (e.g., databases, APIs).
    2. **Transforming** the data into a structured format suitable for analysis.
    3. **Loading** the data into a Data Warehouse for business intelligence and analysis.
    """)

    # Benefits of ETL
    st.write("### Benefits of ETL:")
    st.write("""
    - Data cleaning and validation
    - Data transformation for better insights
    - Centralized data storage
    """)

    # Use columns to organize content
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Data Extraction")
        st.write("""
        Data is extracted from various **sources** including relational databases, 
        APIs, files, and more. This raw data is then prepared for the next steps.
        """)

    with col2:
        st.subheader("Data Transformation")
        st.write("""
        During the transformation phase, data is cleaned, filtered, 
        and formatted to meet the business requirements for analysis.
        """)

    # Expander to explain "Data Loading"
    with st.expander("Data Loading Explanation"):
        st.write("""
        In the loading phase, the transformed data is loaded into a **Data Warehouse** 
        or **Data Lake** to facilitate long-term storage and querying for reporting purposes.
        """)

# Section 3: Data Models
elif topic_option == "Data Models":
    st.header("Data Models in Data Warehousing")
    st.write("""
    There are various types of **Data Models** used in data warehousing:
    1. **Star Schema**: A central fact table surrounded by dimension tables.
    2. **Snowflake Schema**: An extension of the star schema where dimension tables are normalized.
    3. **Galaxy Schema**: A complex model with multiple fact tables sharing dimension tables.
    """)

    # Using tabs for organized content
    tab1, tab2, tab3 = st.tabs(["Star Schema", "Snowflake Schema", "Galaxy Schema"])

    with tab1:
        st.subheader("Star Schema")
        st.write("""
        The **Star Schema** consists of a central fact table and surrounding dimension tables. 
        It is easy to understand and supports high-performance querying.
        """)

    with tab2:
        st.subheader("Snowflake Schema")
        st.write("""
        The **Snowflake Schema** is a more complex version of the star schema, where the dimension tables are further normalized.
        This reduces data redundancy but can result in more complex queries.
        """)

    with tab3:
        st.subheader("Galaxy Schema")
        st.write("""
        The **Galaxy Schema** involves multiple fact tables that share dimension tables. 
        It is more complex and is suited for large, multi-dimensional data systems.
        """)

# Section 4: Data Governance
elif topic_option == "Data Governance":
    st.header("Data Governance in Enterprise Data Management")
    st.write("""
    **Data Governance** refers to the management of data availability, usability, integrity, and security in an organization.
    """)

    st.write
