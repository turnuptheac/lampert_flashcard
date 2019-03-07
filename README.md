FlashCards

Final notes:

1. You may find it difficult to test that cards in bin 11 never show up, and that the correct message displays when all cards are either "hard to remember" or in bin 11. I had originally planned to wire up the Django admin interface so that you could force cards into bins for testing purposes, but I hit the six hour mark first. If you'd like, I can put in another few minutes to write and deploy this functionality. 

2. The search functionality simply filters words that start with the query text. It does not trim any whitespace, search word definitions, or search in the middle of any words. Given the limited time constraints, I chose this solution due to its simplicity and its decent performance in MySQL. 

3. When no cards exist at all, the application displays instructions to the end user instead of warning the user that they are "permanently done." This was not in the original specification, but I thought its low effort and considerable added value warranted its addition. 

4. The bin icon and failure icons still lack proper clarification. I couldn't think of a simple way to do this in a manner that worked for both desktop and mobile applications, so I left it as a future enhancement. 

5. The infrastructure and deployments still require some work to make them "production ready." They currently support zero-downtime deployments, automatic failover, identical and low-overhead production and development environments, backups, and rollbacks. It uses Django's development server in production, however, instead of leveraging any of the stable and secure alternatives. 

6. If you're wondering why I chose to exclude Javascript from this application, it's largely due my development approach. Given the simplicity of the requirements, building a single page application did not seem to add any benefit to the end user. It would have degraded load time, unnecessarily complicated the code for future developers, and added dependencies to more third-party libraries. Rather than approaching this project as a way to showcase how much functionality I could build in six hours, I chose to approach it as a way to showcase how I actually work within constraints. 

Given a strict, six hour deadline, I addressed the areas of greatest uncertainty first, as they had the highest chance of imposing delays. Understanding and getting confirmation of both explicit and implicit requirements had the highest initial uncertainty; ensuring the final interface actually satisfied the needs of its audience had the next highest uncertainty. After that, it was all math, which had low uncertainty with a predictable implementation time. 
