# Travel Itinerary Planner

The **Travel Itinerary Planner** is an AI-powered application that generates personalized day trip itineraries. Just enter the city you want to visit and your interests, and the planner will create an itinerary tailored to your preferences.

---

## Features
- **Personalized Itinerary**: Get a custom day trip itinerary based on your interests and selected city.
- **User-Friendly Interface**: Interact with the planner through an intuitive Gradio-powered UI.
- **Powered by LLM**: Leverages the **Llama 3.3-70B Versatile** model for intelligent itinerary generation.

---

## Requirements

- Python 3.10 or later
- The following Python libraries:
  - `os`
  - `dotenv`
  - `typing`
  - `langgraph`
  - `langchain-core`
  - `langchain-groq`
  - `IPython`
  - `gradio`

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/travel-itinerary-planner.git
   cd travel-itinerary-planner
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**:
   Create a `.env` file in the project root and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**:
   ```bash
   python ui.py
   ```

---

## Usage

1. Launch the application, and the Gradio interface will open in your web browser.
2. Enter the city you plan to visit in the **City** textbox.
3. List your interests, separated by commas, in the **Interests** textbox.
4. View your personalized itinerary in the output section.

---

## Code Overview

### Key Components

1. **PlannerState**:
   - A custom `TypedDict` that holds the state of the planner, including messages, city, interests, and the generated itinerary.

2. **Functions**:
   - `input_city`: Processes the city input.
   - `input_interest`: Processes the interests input.
   - `create_itinerary`: Generates the itinerary using the LLM.

3. **LLM Integration**:
   - Uses `ChatGroq` to interact with the **Llama 3.3-70B Versatile** model for creating itineraries.

4. **Gradio Interface**:
   - A user-friendly interface built with Gradio for seamless interaction.

---

## Example

1. Input:
   - **City**: Paris
   - **Interests**: Museums, art galleries, historic sites

2. Output:
   Final itinerary:
For a day trip to Paris focused on museums, art galleries, and historic sites, consider the following itinerary:

* 9:00 AM - 10:00 AM: Start the day at the **Louvre Museum**, one of the world's largest and most famous museums. Explore the impressive collection of art and artifacts from ancient civilizations to the 19th century, including the Mona Lisa.
* 10:30 AM - 12:30 PM: Visit the **Musée d'Orsay**, home to an extensive collection of Impressionist and Post-Impressionist art, including works by Monet, Renoir, and Van Gogh.
* 1:00 PM - 2:30 PM: Take a break for lunch at a charming café near the **Seine River**, such as Café de Flore or Les Deux Magots. Enjoy the scenic views of the river and the city.
* 3:00 PM - 5:00 PM: Explore the **Sainte-Chapelle**, a stunning Gothic chapel known for its breathtaking stained-glass windows, and the **Conciergerie**, a historic site that once served as a royal palace and prison.
* 5:30 PM - 7:00 PM: End the day with a visit to the **Montmartre neighborhood**, famous for its bohemian vibe, street artists, and stunning views of the city from the top of the hill. Visit the **Basilique du Sacré-Cœur**, a beautiful white church perched on the hill.

This itinerary provides a mix of world-class museums, historic sites, and charming neighborhoods, and is a great way to experience the best of Paris in a day.


---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request for review.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Thanks to [LangGraph](https://langgraph.ai/) and [LangChain](https://www.langchain.com/) for providing excellent tools for LLM integration.
- Gradio for the user-friendly interface.

---

Happy traveling! 🌍
