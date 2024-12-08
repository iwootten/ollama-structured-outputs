import ollama from 'ollama';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const City = z.object({
    name: z.string(),
    country: z.string(),
});

const Cities = z.object({
    cities: z.array(City)
})

const response = await ollama.chat({
    model: 'llama3.2',
    messages: [{ role: 'user', content: 'List 5 cities from around the world and their countries' }],
    format: zodToJsonSchema(Cities),
});

const cities = Cities.parse(JSON.parse(response.message.content));

console.log(cities);