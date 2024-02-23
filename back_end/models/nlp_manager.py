#!/usr/bin/env python3
import spacy

class NLPManager:
    """
    NLPManager class for natural language processing tasks using spaCy.

    Attributes:
        nlp (spacy.Language): The spaCy language model loaded for English text processing.

    Methods:
        process_input(user_input):
            Processes the user input using the spaCy language model.

        extract_entities(doc):
            Extracts entities from the spaCy processed document.

        analyze_greeting(doc):
            Analyzes the input document for common greetings and responds accordingly.

        analyze_mission_vision(doc):
            Analyzes the input document for keywords related to mission or vision and provides corresponding information.

        analyze_scia_values(doc):
            Analyzes the input document for keywords related to SCIA values and provides relevant scenarios.

        get_scenario_for_value(value):
            Retrieves a scenario description for a given SCIA value.

    """

    def __init__(self):
        """
        Initializes the NLPManager with the spaCy language model for English text processing.
        """
        self.nlp = spacy.load("en_core_web_sm")

    def process_input(self, user_input):
        """
        Processes the user input using the spaCy language model.

        Args:
            user_input (str): The input text to be processed.

        Returns:
            spacy.Doc: The processed spaCy document.
        """
        doc = self.nlp(user_input)
        return doc

    def extract_entities(self, doc):
        """
        Extracts entities from the spaCy processed document.

        Args:
            doc (spacy.Doc): The processed spaCy document.

        Returns:
            list: A list of extracted entity texts.
        """
        entities = [ent.text for ent in doc.ents]
        return entities

    def analyze_greeting(self, doc):
        """
        Analyzes the input document for common greetings and responds accordingly.

        Args:
            doc (spacy.Doc): The processed spaCy document.

        Returns:
            str or None: A greeting response or None if no greeting is detected.
        """
        greetings = ["hi", "hello", "hey"]
        for token in doc:
            if token.lower_ in greetings:
                return "Hello there! How can I assist you today :)?"
        return None

    def analyze_mission_vision(self, doc):
        """
        Analyzes the input document for keywords related to mission or vision and provides corresponding information.

        Args:
            doc (spacy.Doc): The processed spaCy document.

        Returns:
            str or None: Information about the mission or vision or None if no relevant keywords are found.
        """
        mission_keywords = ["mission"]
        vision_keywords = ["vision"]

        if any(keyword in doc.text.lower() for keyword in mission_keywords):
            return "To propel Africa's prosperity by connecting its people, cultures and markets."
        elif any(keyword in doc.text.lower() for keyword in vision_keywords):
            return "To be Africa's preferred and sustainable Aviation group."
        else:
            return None

    def analyze_scia_values(self, doc):
        """
        Analyzes the input document for keywords related to SCIA values and provides relevant scenarios.

        Args:
            doc (spacy.Doc): The processed spaCy document.

        Returns:
            str or None: A scenario description for the detected SCIA value or None if no relevant keywords are found.
        """
        scia_keywords = ["safety", "customer obsession", "integrity", "accountability"]

        for keyword in scia_keywords:
            if keyword in doc.text.lower():
                value = keyword.capitalize()
                meaning = self.get_scenario_for_value(keyword)
                return f"{value}: {meaning}"
        return None

    def get_scenario_for_value(self, value):
        """
        Retrieves a scenario description for a given SCIA value.
    
        Args:
            value (str): The SCIA value for which the scenario is requested.
    
        Returns:
            str: A scenario description or a default message if the value is not recognized.
        """
        scenarios = {
            "safety": " Safety is the foundation of everything we do.",
            "customer obsession": " We commit to creating positive memorable experiences for our customers.",
            "integrity": "We shall be ethical and trustworthy in all our engagements and we shall treat each person with respect.",
            "accountability": "We take initiative and responsibility for our actions, decisions and results."
        }
        default_message = "I don't have an answer for that, sorry."
    
        # Get the scenario for the given value
        scenario = scenarios.get(value.lower(), default_message)
    
        # Remove the value and the colon from the scenario to avoid repetition
        scenario_without_value = scenario.replace(value.lower() + ":", "").strip()
    
        return scenario_without_value if scenario_without_value else default_message
    
