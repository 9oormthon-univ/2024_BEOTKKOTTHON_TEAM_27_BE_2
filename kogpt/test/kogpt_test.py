import requests
import kogpt.config as config
import json

REST_API_KEY = config.REST_API_KEY

prompt_message = "정보: 나는 <맛있는 버블티 가게>를 운영하고 있는 사장이야. \
                    경기도 용인시 기흥구에 위치하고 있어. \
                    얼그레이 밀크티이라는 신메뉴가 출시되었어. \
                    인스타그램에 홍보 글을 올리고 싶어. \
                    20대 남자를 타깃으로 하고 있어. \
                    '밀크폼이 올라간 밀크티'를 강조해서 홍보하고 싶어. \
                    예시: 안녕하세요! 용인시 기흥구에 위치한 <맛있는 버블티 가게>입니다. 이번에 새롭게 출시된 얼그레이 밀크티로 여러분을 초대합니다. 우리의 특별한 밀크폼이 올라간 이 티는 입안을 감미롭게 만들어줄 것입니다. 산뜻한 얼그레이 향과 부드러운 우유의 조화는 당신의 입맛을 만족시킬 것입니다. 이제 당신도 새로운 맛의 세계로 여행을 떠나보세요. 얼그레이 밀크티와 함께 매혹적인 맛을 경험해보세요! \
                    요청: 정보와 예시를 바탕으로 광고 글을 1개 작성해줘! 300자를 넘기지마. 그리고, 공손한 말투로 만들어줘.\
                    광고 글:"

for temperature in [0.1, 0.2, 0.3]:
    for top_p in [0.1, 0.2, 0.3]:
        r = requests.post(
            'https://api.kakaobrain.com/v1/inference/kogpt/generation',
            json={
                'prompt': prompt_message,
                'max_tokens': 500,
                'temperature': temperature,
                'top_p': top_p,
                'n': 1
            },
            headers={
                'Authorization': 'KakaoAK ' + REST_API_KEY,
                'Content-Type': 'application/json'
            }
        )

        response = json.loads(r.content)

        print(f"Temperature: {temperature}, Top_p: {top_p}")
        print(response["generations"][0]["text"])
        print("=" * 50)