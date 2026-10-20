# Evaluation Plan

Use `data/evaluation_questions.csv` as a starting set, then add questions from the actual documents you plan to demonstrate.

For each question, manually record:
- Whether the correct source passage was retrieved in the top 4 results
- Whether the answer is factually supported by the retrieved passage
- Whether the assistant admits when evidence is insufficient
- Whether the named source is correct
- Approximate response time and any errors

Suggested metrics:
- Retrieval hit rate@4 = questions with a relevant passage in top 4 / total questions
- Grounded answer rate = answers judged supported by retrieved evidence / total answered questions
- Abstention quality = unsupported questions for which the system correctly says evidence is insufficient / unsupported questions tested

Do not publish metrics until you have run the tests and recorded the results.
