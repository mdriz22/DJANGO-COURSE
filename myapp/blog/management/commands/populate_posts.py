from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command inserts post data"
    def handle(self, *args: Any, **options: Any):
        
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

        content =[
               "Exploring the Future of AI: Trends to Watch",
                "Discover the latest advancements in AI technology and how they will shape the future.",
                "The Ultimate Guide to Remote Work Productivity",
                "Tips and strategies to maximize efficiency and balance while working remotely.",
                "10 Simple Recipes for Busy Weeknights",
                "Quick and easy meal ideas to save time without sacrificing flavor.",
                "The Power of Mindfulness in Everyday Life",
                "Learn how practicing mindfulness can improve your mental and emotional well-being.",
                "Top 5 Travel Destinations for 2024",
                "Explore must-visit places that should be on your travel list for the upcoming year.",
                "Mastering Python: Tips for Beginners",
                "Essential tips to get started with Python and accelerate your learning curve.",
                "How to Build a Successful Side Hustle",
                "Actionable steps to turn your passion into a profitable side business.",
                "The Impact of Social Media on Mental Health",
                "Examine the effects of social media on mental well-being and how to manage it.",
                "Designing the Perfect Home Office Space",
                "Create a functional and inspiring workspace with these design ideas.",
                "Breaking Down the Basics of Cryptocurrency",
                "A beginner's guide to understanding cryptocurrency and how it works.",
                "The Benefits of Daily Exercise: A Complete Guide",
                "Discover how regular exercise boosts physical and mental health.",
                "How to Create Stunning Visuals for Your Website",
                "Tips on designing eye-catching visuals that enhance user engagement.",
                "Understanding Big Data: An Introduction for Everyone",
                "Learn the basics of big data and its applications in today’s digital world.",
                "The Art of Personal Branding: 5 Key Strategies",
                "Effective strategies to build and grow your personal brand.",
                "Sustainable Living: Simple Changes for a Greener Lifestyle",
                "Small lifestyle adjustments you can make to live more sustainably.",
                "Why Networking is Essential for Career Growth",
                "Understand the importance of networking and how it can advance your career.",
                "Top 10 Books Every Entrepreneur Should Read",
                "A curated list of must-read books for aspiring and seasoned entrepreneurs.",
                "The Role of Blockchain in Cybersecurity",
                "Explore how blockchain technology enhances security in digital networks.",
                "How to Boost Your SEO Rankings in 2024",
                "Proven techniques to improve your website’s search engine ranking in the new year.",
                "Developing Healthy Habits: A Step-by-Step Approach",
                "A practical guide to forming and maintaining habits that support a healthier life."

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



        for title,content, img_url in zip(titles , content , img_urls):
            Post.objects.create(title = title, content=content, img_url=img_url)



        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))    

              