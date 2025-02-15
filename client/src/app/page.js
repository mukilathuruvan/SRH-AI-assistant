// "use client";
// import { useState, useRef } from "react";

// const ChatInput = ({ onSendMessage }) => {
//   const [prompt, setPrompt] = useState("");
//   const [image, setImage] = useState(null);
//   const [video, setVideo] = useState(null);
//   const [audio, setAudio] = useState(null);
//   const audioRef = useRef(null);

//   const handlePromptChange = (e) => {
//     setPrompt(e.target.value);
//   };

//   const handleImageChange = (e) => {
//     setImage(e.target.files[0]);
//   };

//   const handleVideoChange = (e) => {
//     setVideo(e.target.files[0]);
//   };

//   const handleAudioChange = (e) => {
//     setAudio(e.target.files[0]);
//   };

//   const handleAudioRecord = () => {
//     if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
//       navigator.mediaDevices
//         .getUserMedia({ audio: true })
//         .then((stream) => {
//           const recorder = new MediaRecorder(stream);
//           recorder.start();

//           const chunks = [];
//           recorder.ondataavailable = (e) => chunks.push(e.data);
//           recorder.onstop = () => {
//             const blob = new Blob(chunks, { type: "audio/wav" }); // Or appropriate type
//             setAudio(blob);
//           };

//           audioRef.current.onclick = () => {
//             recorder.stop();
//             audioRef.current.onclick = handleAudioRecord; // Reset onclick
//             audioRef.current.textContent = "Record Audio";
//           };
//           audioRef.current.onclick(); // Stop Recording
//           audioRef.current.textContent = "Stop Recording";
//         })
//         .catch((err) => console.error("Error accessing microphone:", err));
//     }
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     const formData = new FormData();
//     formData.append("prompt", prompt);
//     if (image) formData.append("image", image);
//     if (video) formData.append("video", video);
//     if (audio) formData.append("audio", audio);

//     try {
//       const response = await fetch("http://localhost:8080/api/chat", {
//         method: "POST",
//         body: formData,
//       });

//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`);
//       }

//       const data = await response.json();
//       onSendMessage(data);
//       setPrompt("");
//       setImage(null);
//       setVideo(null);
//       setAudio(null);
//     } catch (error) {
//       console.error("Error sending message:", error);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <input
//         type="text"
//         value={prompt}
//         onChange={handlePromptChange}
//         placeholder="Enter your message..."
//       />
//       <input type="file" accept="image/*" onChange={handleImageChange} />
//       <input type="file" accept="video/*" onChange={handleVideoChange} />
//       <button type="button" ref={audioRef} onClick={handleAudioRecord}>
//         Record Audio
//       </button>
//       <button type="submit">Send</button>
//     </form>
//   );
// };

// const HomePage = () => {
//   const [messages, setMessages] = useState([]);

//   const handleSendMessage = (data) => {
//     setMessages([
//       ...messages,
//       {
//         type: "user",
//         content: data.prompt,
//         image: data.image,
//         video: data.video,
//         audio: data.audio,
//       },
//       { type: "bot", content: data.gemini, chatgpt: data.chatgpt },
//     ]);
//   };

//   return (
//     <div>
//       {/* Display chat messages */}
//       {messages.map((message, index) => (
//         <div key={index}>
//           <p>Type: {message.type}</p>
//           <p>Content: {message.content}</p>
//           {message.image && (
//             <img src={URL.createObjectURL(message.image)} alt="User Image" />
//           )}
//           {message.video && (
//             <video src={URL.createObjectURL(message.video)} controls />
//           )}
//           {message.audio && (
//             <audio src={URL.createObjectURL(message.audio)} controls />
//           )}
//           {message.chatgpt && <p>ChatGPT: {message.chatgpt}</p>}
//         </div>
//       ))}
//       <ChatInput onSendMessage={handleSendMessage} />
//     </div>
//   );
// };

// export default HomePage;

const page = () => {
  return <div>page</div>;
};

export default page;
