# Smart Customer Support System

This project demonstrates the setup of an AWS-powered **Smart Customer Support System** using **Amazon Connect**, **Lex**, **Polly**, and **Lambda**. The system routes customer calls, provides automated responses using Lex bots, and can escalate to a live agent when needed.

## Project Overview

The goal of this project is to create an automated customer support system where:
- Customers can interact with a virtual agent for FAQs.
- The system routes calls based on customer inputs (e.g., "Order Status" or "Return Policy").
- Polly is used for voice synthesis, and Lambda adds automation for fetching customer data.
- The system escalates to a live agent when needed.

### Components Used:
1. **Amazon Connect**: Used to set up the contact center for voice-based customer interactions.
2. **Amazon Lex**: Used for creating conversational chatbots to handle FAQs.
3. **Amazon Polly**: Used for converting text into lifelike speech.
4. **AWS Lambda**: Used for custom logic (e.g., fetching customer data from an external service).
5. **Amazon CloudWatch**: For logging and monitoring the system.

## Steps to Set Up the Project

### 1. Set up Amazon Connect Instance
- Go to **Amazon Connect** in AWS Console.
- Create a **new instance** and configure the basic settings (choose a region, select contact flow options, etc.).
  
### 2. Create Lex Bot for Handling FAQs
- Go to **Amazon Lex** in AWS Console.
- Create a new Lex bot.
- Define intents like **"Order Status"**, **"Return Policy"**, etc.
- Set up the Lex bot with sample phrases that users will say, such as **"What is my order status?"**.

### 3. Set up Polly for Voice Responses
- In **Amazon Connect**, go to your contact flow and add a **Play Prompt** block.
- In the Play Prompt block, you can add text that you want Polly to convert to speech. For example: "Welcome to ShopEasy, how may I assist you today?"
- Use **Polly** in the contact flow settings to select the voice and language.

### 4. Add Lambda Function for Custom Routing Logic
- Go to **AWS Lambda** in the console.
- Create a Lambda function to implement any business logic you need (for example, fetching customer data from an external API).
- Attach the Lambda function to your Amazon Connect instance by adding it in the contact flow.

### 5. Build Contact Flow in Amazon Connect
- Create a contact flow using **Amazon Connect**'s drag-and-drop interface.
- Add the **Play Prompt**, **Get Customer Input**, **Transfer to Agent**, and **Invoke Lambda** blocks.
- Configure each block to handle various scenarios (e.g., timeout, error handling, etc.).
- Publish the flow.

### 6. Testing and Deployment
- Once the configuration is done, test the setup by calling the Amazon Connect phone number.
- Verify that the Lex bot answers correctly, Polly reads out the responses, and Lambda is triggered when needed.
- Make adjustments based on feedback.



