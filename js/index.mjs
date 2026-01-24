import OpenAI from "openai";
const client = new OpenAI();

//#region Simple Request
const response = await client.responses.create({
    model: "gpt-5-nano",
    input: "how to become AI Engineer?",
});

console.log(response.output_text);
//#endregion Simple Request

//#region Streaming
const stream = await client.responses.create({
    model: 'gpt-5-nano',
    input: 'Say "Sheep sleep deep" ten times fast!',
    stream: true,
});

for await (const event of stream) {
    console.log(event);
}
//#endregion Streaming