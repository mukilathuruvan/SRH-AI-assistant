const API_URL = "http://localhost:8080/api";

export const chatWithBot = async (message) => {
  try {
    const response = await fetch(`${API_URL}/ask`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: message }),
    });

    const data = await response.json();

    return data;
  } catch (error) {
    return "Sorry, I don't understand. Please try again.";
  }
};
