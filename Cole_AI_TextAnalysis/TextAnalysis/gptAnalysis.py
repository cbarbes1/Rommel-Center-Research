import openai
import os

API_KEY = os.getenv('OPENAI_API_KEY')



response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={"type":"json_object"},
    messages = [
        {"role": "system", "content": "You are a helpful topic model. Every prompt will be an abstract, your job is to analyze the abstract and extract a list of possible topics for it. The topics start at a high level and get more detailed as you go. The topics for example should be like Computer Science or Business etc..., output should be JSON with the root being the abstract"},
        {"role": "user", "content": "The extant research sheds light on the vital role of co-creation in online healthcare communities (OHCs) as nascent peer-to-peer co-creation platforms in public health and well-being. However, more investigation of the underlying factors affecting patient value co-creation in OHCs is required. This study relies on the socio-technical theory to identify the social and technical factors that impact healthcare users' intention to co-create value. Analysis of survey data gathered from users of Top 10 healthcare-based pages on Facebook indicated that both social and technical factors are salient in the prediction of value co-creation in OHCs. More specifically, social support and its antecedents (i.e., perceived privacy risk and social media interactivity), as well as government IT infrastructures and perceived control of information, are found to be the critical antecedents of value co-creation intention. However, social support emerged as the most potent predictor of value co-creation relative to government IT infrastructures and control of information. The theoretical and practical contributions of the findings are discussed."},
    ]
)

print(response.choices[0].message.content)