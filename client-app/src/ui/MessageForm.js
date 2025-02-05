"use client";

import { useMessages } from "@/providers/MessageContextProvider";
import { useState } from "react";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";

const MessageForm = () => {
  const [content, setContent] = useState("");
  const { addMessage } = useMessages();

  const handleSubmit = async (e) => {
    e.preventDefault();
    addMessage(content);
    setContent("");
  };

  return (
    <form
      className="relative mx-8 rounded-xl bg-gray-200"
      onSubmit={handleSubmit}
    >
      <div className="supports-backdrop-blur:bg-white/95 h-[130px] rounded-xl p-5 backdrop-blur">
        <Textarea
          name="content"
          placeholder="Enter your message here..."
          rows={3}
          value={content}
          autoFocus
          className="border-0 !p-3 text-gray-900 shadow-none ring-1 ring-gray-300/40 backdrop-blur focus:outline-none focus:ring-gray-300/80 dark:bg-gray-800/80 dark:text-white dark:placeholder-gray-400 dark:ring-0"
          onChange={(e) => setContent(e.target.value)}
        />
        <div className="absolute top-9 bottom-0 right-8">
          <div className="flex">
            <Button className="px-8 py-4" type="submit" size="small">
              Send
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                strokeWidth={1.5}
                stroke="currentColor"
                className="ml-1 h-4 w-4"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"
                />
              </svg>
            </Button>
          </div>
        </div>
      </div>
    </form>
  );
};

export default MessageForm;
