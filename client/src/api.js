const API_URL = "http://localhost:8080/api";

export const chatWithBot = async (formData) => {
  try {
    const response = await fetch(`${API_URL}/chat`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    return data;
  } catch (error) {
    return "Sorry, I don't understand. Please try again.";
  }
};
