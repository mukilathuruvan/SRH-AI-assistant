"use client";

import { chatWithBot } from "@/api";
import { createContext, useContext, useEffect, useState } from "react";

const ChatsContext = createContext({});

export function MessagesProvider({ children }) {
  const [gptMessages, setGptMessages] = useState([]);
  const [geminiMessages, setGeminiMessages] = useState([]);

  const [isLoadingAnswer, setIsLoadingAnswer] = useState(false);

  useEffect(() => {
    const initializeChat = () => {
      const systemMessage = {
        role: "system",
        content: "You are ChatGPT, a large language model trained by OpenAI.",
      };
      const welcomeMessage = {
        role: "assistant",
        content: "Hi, How can I help you today?",
      };
      setGptMessages([systemMessage, welcomeMessage]);
      setGeminiMessages([systemMessage, welcomeMessage]);
    };

    if (!gptMessages?.length) {
      initializeChat();
    }
  }, [gptMessages?.length, geminiMessages?.length, setGptMessages]);

  const addMessage = async (userContent) => {
    setIsLoadingAnswer(true);
    try {
      setGptMessages([...gptMessages, userContent]);
      setGeminiMessages([...geminiMessages, userContent]);

      const { gemini_response = null, gpt_response = null } = await chatWithBot(
        userContent.content
      );
      if (!gemini_response && !gpt_response) return;

      setGeminiMessages((messages) => [
        ...messages,
        { ...gemini_response, role: "assistant" },
      ]);

      setGptMessages((messages) => [
        ...messages,
        { ...gpt_response, role: "assistant" },
      ]);
    } catch (error) {
      console.error(error);
    } finally {
      setIsLoadingAnswer(false);
    }
  };

  return (
    <ChatsContext.Provider
      value={{ gptMessages, geminiMessages, addMessage, isLoadingAnswer }}
    >
      {children}
    </ChatsContext.Provider>
  );
}

export const useMessages = () => {
  if (useContext(ChatsContext) === undefined) {
    throw new Error("useMessages must be used within a MessagesProvider");
  }
  return useContext(ChatsContext);
};
