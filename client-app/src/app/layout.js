import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { MessagesProvider } from "@/providers/MessageContextProvider";
import MessagesList from "@/ui/MessageList";
import MessageForm from "@/ui/MessageForm";
import LayoutProvider from "@/providers/LayoutProvider";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <MessagesProvider>
          <LayoutProvider>
            <MessagesList />
            <div className="fixed bottom-0 right-0 left-0">
              <MessageForm />
            </div>
          </LayoutProvider>
        </MessagesProvider>
      </body>
    </html>
  );
}
