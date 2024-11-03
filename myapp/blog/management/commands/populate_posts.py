from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "This command inserts post data"
    def handle(self, *args: Any, **options: Any):
        #Delete existing data
        Post.objects.all().delete()
        titles =[
                "Exploring the Future of AI: Trends to Watch",
                "The Ultimate Guide to Remote Work Productivity",
                "10 Simple Recipes for Busy Weeknights",
                "The Power of Mindfulness in Everyday Life",
                "Top 5 Travel Destinations for 2024",
                "Mastering Python: Tips for Beginners",
                "How to Build a Successful Side Hustle",
                "The Impact of Social Media on Mental Health",
                "Designing the Perfect Home Office Space",
                "Breaking Down the Basics of Cryptocurrency",
                "The Benefits of Daily Exercise: A Complete Guide",
                "How to Create Stunning Visuals for Your Website",
                "Understanding Big Data: An Introduction for Everyone",
                "The Art of Personal Branding: 5 Key Strategies",
                "Sustainable Living: Simple Changes for a Greener Lifestyle",
                "Why Networking is Essential for Career Growth",
                "Top 10 Books Every Entrepreneur Should Read",
                "The Role of Blockchain in Cybersecurity",
                "How to Boost Your SEO Rankings in 2024",
                "Developing Healthy Habits: A Step-by-Step Approach",

                ]

        content = [
                "Discover the latest advancements in AI technology and how they will shape the future. From machine learning breakthroughs to innovative applications, explore how AI is transforming industries and our daily lives.",

                "Tips and strategies to maximize efficiency and balance while working remotely. Learn how to create a structured schedule, set boundaries, and utilize productivity tools that keep you focused and engaged.",

                "Quick and easy meal ideas to save time without sacrificing flavor. Discover recipes that require minimal prep and cooking time, yet deliver delicious and nutritious meals for busy days.",

                "Learn how practicing mindfulness can improve your mental and emotional well-being. Understand the benefits of mindfulness techniques such as meditation and deep breathing, and how they can reduce stress and enhance focus.",

                "Explore must-visit places that should be on your travel list for the upcoming year. From hidden gems to iconic landmarks, uncover travel destinations that offer unique experiences and unforgettable memories.",

                "Essential tips to get started with Python and accelerate your learning curve. Gain insights into online resources, coding exercises, and community support that will help you master Python quickly and effectively.",

                "Actionable steps to turn your passion into a profitable side business. Identify your niche, create a business plan, and explore marketing strategies that can help you monetize your skills and interests.",

                "Examine the effects of social media on mental well-being and how to manage it. Understand the impact of online interactions on self-esteem and mental health, and learn strategies for healthy social media usage.",

                "Create a functional and inspiring workspace with these design ideas. Discover tips for organizing your home office, choosing the right furniture, and incorporating personal touches that boost creativity and productivity.",

                "A beginner's guide to understanding cryptocurrency and how it works. Learn about blockchain technology, different types of cryptocurrencies, and tips for safely investing in digital currencies.",

                "Discover how regular exercise boosts physical and mental health. Explore various forms of exercise that can improve mood, enhance cognitive function, and promote overall well-being.",

                "Tips on designing eye-catching visuals that enhance user engagement. Learn about color theory, typography, and design tools that can help you create stunning graphics for websites and social media.",

                "Learn the basics of big data and its applications in today’s digital world. Understand the significance of data analytics, data mining, and how businesses leverage big data to make informed decisions.",

                "Effective strategies to build and grow your personal brand. Discover how to define your brand identity, engage with your audience, and use social media to amplify your presence and credibility.",

                "Small lifestyle adjustments you can make to live more sustainably. Explore eco-friendly habits, such as reducing waste, conserving energy, and supporting local businesses, that contribute to a healthier planet.",

                "Understand the importance of networking and how it can advance your career. Learn how to build meaningful connections, leverage professional platforms, and navigate networking events to expand your opportunities.",

                "A curated list of must-read books for aspiring and seasoned entrepreneurs. Dive into titles that offer valuable insights on entrepreneurship, innovation, and leadership to inspire your journey.",

                "Explore how blockchain technology enhances security in digital networks. Understand the principles of decentralization, cryptography, and how blockchain can protect data integrity in various applications.",

                "Proven techniques to improve your website’s search engine ranking in the new year. Learn about SEO best practices, content optimization, and the importance of backlinks to increase your online visibility.",

                "A practical guide to forming and maintaining habits that support a healthier life. Discover strategies for setting achievable goals, tracking your progress, and overcoming obstacles to create lasting change."

                   ]


        img_urls = [
                "https://picsum.photos/id/1/800/400",
                "https://picsum.photos/id/2/800/400",
                "https://picsum.photos/id/3/800/400",
                "https://picsum.photos/id/4/800/400",
                "https://picsum.photos/id/5/800/400",
                "https://picsum.photos/id/6/800/400",
                "https://picsum.photos/id/7/800/400",
                "https://picsum.photos/id/8/800/400",
                "https://picsum.photos/id/9/800/400",
                "https://picsum.photos/id/10/800/400",
                "https://picsum.photos/id/11/800/400",
                "https://picsum.photos/id/12/800/400",
                "https://picsum.photos/id/13/800/400",
                "https://picsum.photos/id/14/800/400",
                "https://picsum.photos/id/15/800/400",
                "https://picsum.photos/id/16/800/400",
                "https://picsum.photos/id/17/800/400",
                "https://picsum.photos/id/18/800/400",
                "https://picsum.photos/id/19/800/400",
                "https://picsum.photos/id/20/800/400",
                ]

        categories =Category.objects.all()

        for title,content, img_url in zip(titles , content , img_urls):
            category=random.choice(categories)
            Post.objects.create(title = title, content=content, img_url=img_url,Category=category)



        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))    

              