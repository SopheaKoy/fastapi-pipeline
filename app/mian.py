from mcp import ClientSession, stdio_client
from anthropic import Anthropic

def ask_llm(prompt):
    client = Anthropic()
    completion = client.completions.create(
        model="claude-3-sonnet",
        max_tokens=1000,
        prompt=prompt
    )
    return completion.completion

async def main():
    async with stdio_client() as client:
        resources = await client.list_resources()
        video_ids = [resource.split("://")[1] for resource in resources if resource.startswith("transcript://")]

        while True:
            user_query = input("User: ")
            if user_query.lower() == "exit":
                break
            if "video" in user_query.lower():
                video_id = user_query.split()[-1]
                if video_id in video_ids:
                    context = await client.read_resource(f"transcript://{video_id}")
                else:
                    context = "Video not found."
            else:
                context = await client.call_tool("search_transcripts", query=user_query)
            prompt = f"Given the following transcript:\n{context}\nAnswer the question: {user_query}"
            response = ask_llm(prompt)
            print("Assistant:", response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())