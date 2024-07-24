import asyncio

# Simulate the asynchronous model.generate_content method
async def generate_content(description):
    # Replace this with the actual async call to your model
    await asyncio.sleep(1)  # Simulating network delay
    return f"Generated content for: {description}"

async def main():
    descriptions = [
        "Generate Data Scientist Job Description for Facebook, Company Description: Log in to Facebook to start sharing and connecting with your friends, family and people you know.",
        "Generate Data Scientist Job Description for WhereUElevate, Company Description: Where U Elevate: Connecting next-gen innovative workforce with industry.",
        "Generate Data Scientist Job Description for Youtube, Company Description: Enjoy the videos and music you love, upload original content, and share it all with friends, family, and the world on YouTube.",
        "Generate Data Scientist Job Description for Instagram, Company Description: Create an account or log in to Instagram - Share what you're into with the people who get you.",
        "Generate Data Scientist Job Description for Myntra, Company Description: Online Shopping Site for Fashion & Lifestyle in India. India's Fashion Expert brings you a variety of footwear, Clothing, Accessories and lifestyle products for women & men. Best Online Fashion Store *COD *Easy returns and exchanges.",
        "Generate Data Scientist Job Description for Devfolio, Company Description: Participate in a hackathon or even better, host one. Learn new skills, build things & get hired."
    ]

    # Create a list of tasks to run in parallel
    tasks = [generate_content(desc) for desc in descriptions]

    # Await all tasks and gather results
    results = await asyncio.gather(*tasks)

    # Print results
    for result in results:
        print(result)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
