<h2 align="left">BenchScout : A semantic search engine for AI4SE benchmarks</h2>

As part of the contribution of our paper we have proposed [**BenchScout **](https://evalpro.online/search.html). To evaluate the quality of this created tool, we conducted a user study with 22 participants. The study aimed to understand the usability and effectiveness of the tool in finding AI4SE benchmarks. The participants were asked to play around with the tool and provide feedback on their experience. The study was conducted remotely and the participants were asked to complete a survey after using the tool. The survey consisted of questions related to the search functionality, cross-referencing feature, user experience, and feedback. The results of the study are presented below.

For a more detailed analysis of the study, please refer to the paper.

**_Note_**: The results of the open-ended questions are summarized using word clouds. This is to provide a visual representation of the most common responses, other than that, this is not an exhaustive list of responses.

## Participant Background
- **What is your professional background?**
   - **Scale**: 5-point Likert Scale
   - **Results**:
        ```mermaid 
         pie title Number Of Participants
            "Industry" : 9
            "Academia" : 13
        ``` 
-  **What is your role?**
   - **Scale**: Open-ended
   - **Results**:
       ```mermaid
        pie title Roles
        "(Software / Research) (Engineer / Developer)" : 4
        "PhD Candidate" : 5
        "Researcher" : 6
        "Lead Researcher" : 2
        "Student" : 5
       ```
- **How familiar are you with AI4SE benchmarks?**
   - **Scale**: 5-point Likert Scale (1: Not familiar, 5: Very familiar)
   - **Results**: 
       ```mermaid
        xychart-beta
        title "AI4SE Benchmarks Familiarity"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 8
        bar [0, 5, 2, 7, 8]
       ```

- **How many years of experience do you have in this field?**
   - **Scale**: Multiple Choice (<1, 1-3, 3-5, 5+ years)
   - **Results**: 
       ```mermaid
        pie title Years of Experience
        "Less than 1 year" : 5
        "between 1 and 3 years" : 8
        "between 3 and 5 years" : 6
        "5+ years" : 3
       ```
---

## Search Functionality
- **How easy was it to navigate the interface?**
   - **Scale**: 5-point Likert Scale
   - **Results**:  
       ```mermaid
        xychart-beta
        title "General Interface navigability"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 12
        bar [0, 0, 1, 10, 11]
       ```
- **How intuitive was the search functionality?**
   - **Scale**: 5-point Likert Scale (1: Not useful, 5: Extremely useful)
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Search Functionality Intuitiveness"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 12
        bar [0, 1, 3, 11, 7]
       ```
- **How effective was the tool in finding benchmarks?**
   - **Scale**: 5-point Likert Scale
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Effectiveness of Benchmark Search"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 13
        bar [0, 0, 5, 12, 5]
       ```

- **Was the visual evaluation of datasets useful?**
   - **Scale**: 5-point Likert Scale
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Visual Evaluability of Datasets"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 9
        bar [1, 3, 3, 7, 8]
       ```
---

## Cross-referencing Feature

- **How useful was the cross-referencing feature?**
   - **Scale**: 5-point Likert Scale
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Usefulness of Cross-referencing"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 14
        bar [0, 0, 3, 14, 5]
       ```

- **Did the tool help in understanding relationships between benchmarks?**
   - **Scale**: 5-point Likert Scale
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Understandability Benchmark Relationships"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 11
        bar [0, 1, 7, 11, 3]
       ```

- **Was the visual interface for benchmark similarity useful?**
   - **Scale**: 5-point Likert Scale
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Visual Interface for Benchmark Similarity"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 9
        bar [0, 3, 5, 6, 8]
       ```

---

## User Experience & Feedback

- **How would you rate the overall user experience?**
   - **Scale**: 5-point Likert Scale
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Overall User Experience"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 13
        bar [0, 0, 3, 12, 7]
       ```

- **How likely are you to use the tool in your work?**
   - **Scale**: 5-point Likert Scale
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Likelihood of Tool Usage"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 10
        bar [0, 1, 6, 9, 6]
       ```

- **Did you experience any issues or challenges?**
   - **Scale**: Open-ended
   - **Results**: ![Word Cloud](../images/wordCloudIssues.png)

- **What other tools do you use for searching benchmarks?**
   - **Scale**: Open-ended
   - **Results**: ![Word Cloud](../images/wordCloudOtherTools.png)

- **How does this tool compare to others?**
   - **Scale**: 5-point Likert Scale
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Comparison to Other Tools"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 3
        bar [0, 0, 1, 3, 2]
       ```

- **How well does the tool meet the needs of professionals in AI4SE?**
   - **Scale**: Open-ended
   - **Results**:   
       ```mermaid
        xychart-beta
        title "Tool Suitability for AI4SE Professionals"
        x-axis ["1", "2", "3", "4", "5"]
        y-axis "Participant Count" 0 --> 15
        bar [0, 0, 2, 14, 6]
       ```

---
## Additional Comments
- **Do you have any suggestions for improving the tool?**
   - **Scale**: Open-ended
   - **Results**: ![Word Cloud](../images/wordCloudAdditionalFeatures.png)
