This API provides essential endpoints for retrieving real-time information about loadshedding affecting your specific area.
1. Check Loadshedding Status

Retrieve the current loadshedding status in your area. This endpoint allows you to check if there is any active loadshedding.
API Endpoint

    Endpoint: https://loadsheddingchecker.com/api/status
    Request Method: HTTP GET

Response Parameters

    Status: integer
    Description: Current loadshedding status in your area.
    Example Values: 1 (No load shedding), 2 (Stage 1), 3 (Stage 2), 4 (Stage 3), 5 (Stage 4)

2. Retrieve Municipalities List

Get a list of municipalities affected by loadshedding. This endpoint enables you to obtain the names and IDs of municipalities for further queries.
API Endpoint

    Endpoint: https://loadsheddingchecker.com/api/municipalities
    Request Method: HTTP GET

Response Parameters

    Municipality ID: int
    Name: String
    Description: Name of the municipality affected by loadshedding.

3. Get Suburb Information

Retrieve loadshedding details for specific suburbs within a municipality. This endpoint allows you to input your suburb ID and get loadshedding schedules tailored to your area.
API Endpoint

    Endpoint: https://loadsheddingchecker.com/api/suburbs/{suburbId}
    Request Method: HTTP GET

Request Parameters

    Suburb ID: int
    Description: Unique identifier for your suburb within the municipality.

Response Parameters

    Day: String
    Time: String
    Description: Loadshedding schedule for the specific day and time in your suburb.
    Example Values: Wed, 09 Sep, 06:00 - 08:30

4. Get Detailed Schedule

For a more comprehensive loadshedding schedule, use this endpoint to get detailed information about multiple days and time slots affecting your area.
API Endpoint

    Endpoint: https://loadsheddingchecker.com/api/schedule/{suburbId}
    Request Method: HTTP GET

Request Parameters

    Suburb ID: int
    Description: Unique identifier for your suburb within the municipality.

Response Parameters

    Day: String
    Time: String
    Description: Loadshedding schedule for the specific day and time in your suburb.
    Example Values: Wed, 09 Sep, 06:00 - 08:30

Feel free to integrate these endpoints into your Loadshedding Checker App to provide accurate and up-to-date information to your users. If you have any further questions or need assistance, please don't hesitate to contact our support team.