**Introduction**:

This project is part of Software Testing and Analysis, focusing on Load Testing, specifically spike testing. Spike testing is a subfield of load testing used to assess a system's performance under sudden and immediate increases in load. This helps determine how well the system can handle unexpected loads and surges in traffic.

The tests are conducted on the FakeStore API, a public API that provides mock data for testing purposes. Using Locust, we assess the API's performance under various user loads and scenarios.

**Solution**:

We implemented several test scenarios using Locust:

1. Base Load Test: Simulates normal user behavior.

2. Spike Load Test: Tests sudden bursts of user activity.

3. User Creation and Product Search: Tests creating new user accounts and searching for products.

4. Flash Sale Simulation: Simulates high-traffic sales events.

5. Error Handling Under Load: Evaluates response to erroneous requests.

6. API Rate Limit Testing: Verifies rate limiting effectiveness.

7. Geographical Load Testing: Tests performance for users in different regions.

8. Peak Load Simulation: Tests capacity and stability under maximum load.

9. Scenario-Based Load Testing: Mimics typical user journeys.

**Implementation**:
 
1. Ensure Python is installed on your system.
   
2. Install Locust using pip install locust 

3. Install requirements using pip install -r requirements.txt

4. Run test and monitor performance: locust -f locustfile.py --host=https://fakestoreapi.com/

5. Configure the number of users and spawn rate to simulate different load scenarios.


