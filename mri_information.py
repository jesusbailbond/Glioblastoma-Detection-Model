import streamlit as st
from PIL import Image

def mri_information():
    # Title for the Page
    st.title("Comprehensive Guide to Head MRI: Preparation, Procedure, and Insights")
    
    # Introductory Text
    st.markdown("""
    A head MRI provides doctors with detailed images of your brain to diagnose or rule out various medical conditions. 
    By combining advanced imaging techniques with your medical history, it’s a critical step in understanding your symptoms and creating a treatment plan.
    """)
    
    # Image with Caption
    st.image(
        "C:/Users/Jordan/Desktop/Data Science Folders/PROJECT/Deploying_Project/streamlit_img/quick-fact.webp",  # Replace with your actual image path
        caption="Illustration of MRI process",
        width=700  # Adjust to fit your layout
    )
    
    # Subtitle
    st.title(" Why Would You Need a Head MRI?")
    
    # Content for MRI Use Cases
    st.markdown("""
    Doctors may recommend a head MRI to investigate specific symptoms or diagnose a range of conditions. 
    This imaging test offers exceptional detail about the brain’s structure, blood flow, and surrounding fluids.

    ### Common Reasons for a Head MRI
    - **Diagnosing Conditions**:  
      - Infections  
      - Stroke  
      - Brain tumors  
      - Multiple sclerosis  
      - Hemorrhage or brain bleeding  
      - Hydrocephalus (fluid buildup in the brain)  
      - Pituitary gland disorders  
      - Brain aneurysms or blood vessel issues  
      - Spinal cord injuries  
      - Developmental abnormalities  
      - Blood clots or cysts  
      - Hormonal imbalances    

   - **Investigating Symptoms**:  
     - Vision problems or dizziness  
     - Chronic headaches or seizures  
     - Muscle weakness, tingling, or numbness  
     - Hearing loss or speaking difficulties  
     - Changes in behavior, cognition, or mood  

   An MRI can help determine the cause of these symptoms by examining the brains structure, blood vessels, and any abnormal growths or lesions.  

   --- 
   """)
    
   #Subtitle 

    st.title("What Does a Brain MRI Show?")
    st.image(
        "C:/Users/Jordan/Desktop/Data Science Folders/PROJECT/Deploying_Project/streamlit_img/brain-MRI.jpg", 
        caption="Illustration of MRI process",
        width=700 
    )
    st.markdown("""
   A head MRI provides detailed cross-sectional images of the brain, allowing doctors to observe:  

   1. **Brain Lesions**:  
      - Abnormal spots in the brain that may indicate multiple sclerosis, tumors, or infections.  

   2. **Brain Structures**:  
      - **Cerebrum**: Functions like movement, emotions, reasoning, vision, and hearing.  
      - **Brainstem**: Governs involuntary actions such as heart rate and hunger.  
      - **Cerebellum**: Coordinates muscle movement, balance, and posture.  

   3. **Blood Flow and Fluid Dynamics**:  
      - Highlights abnormalities in arteries, veins, or fluid buildup.  

   ---
                """)

    st.title(" How to Prepare for a Head MRI")
    st.markdown("""
   ### **Diet and Medications**  
   - Eat and take medications as usual unless otherwise instructed.  
   - For specific MRIs, fasting for 4 to 6 hours may be required.  

   ### **Metal and Electronics**  
   - Remove all metal objects to prevent interference or safety risks:  
     - Jewelry, body piercings, hairpins, eyeglasses  
     - Metal fasteners (zippers, buckles, etc.)  
     - Removable dental work or hearing aids  

   - Avoid products containing metal particles (makeup, nail polish, hair products).  

   ### **Medical Considerations**  
   - Inform your doctor if you have:  
     - Implants or metal fragments (e.g., stents, pacemakers, joint replacements).  
     - Kidney or liver disease (due to gadolinium contrast agents).  
     - Claustrophobia (ask about sedation or open MRI options).  
     - Pregnancy (gadolinium is generally avoided unless necessary).  

   ---
                """)

    st.image(
        "C:/Users/Jordan/Desktop/Data Science Folders/PROJECT/Deploying_Project/streamlit_img/mri-image.jpg", 
        caption="Illustration of MRI process",
        width=700 
    )

    st.title("What to Expect During a Head MRI")  
    st.markdown("""
   1. **Before the Scan**  
      - Change into a hospital gown or metal-free clothing.  
      - Secure personal belongings in a locker.  

   2. **Entering the MRI Room**  
      - The MRI machine resembles a large tube with open ends.  

   3. **Lying on the Table**  
      - You will lie on a sliding table with your head secured for stability.  

   4. **Receiving Contrast (if needed)**  
      - Gadolinium may be injected via IV for clearer images.  

   5. **Handling Noise**  
      - Loud knocking/thumping noises are normal; headphones or earplugs will be provided.  

   6. **Staying Still**  
      - Remain still for clear images; you may be asked to hold your breath briefly.  

   7. **Communication**  
      - You will communicate with the technologist via a speaker system.  

   8. **After the Scan**  
      - IVs (if used) will be removed, and you will be assisted off the table.  

   ---
""")
    st.title(" Key Benefits of an MRI")
    st.markdown("""  
   - No radiation exposure (unlike X-rays or CT scans).  
   - Exceptional clarity for soft tissues, blood vessels, and fluids.  
   - Early and accurate diagnosis of complex conditions.  

   ---

   ##  Tips for a Comfortable Experience  
   - Opt for an **open or short-bore MRI machine** if claustrophobia is a concern.  
   - Bring a trusted person to accompany you.  
   - Consult your doctor about sedatives if needed.  

   By understanding what to expect and preparing accordingly, you can approach your MRI with confidence, ensuring the best results for your diagnosis and treatment plan.  
   """)