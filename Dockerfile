FROM sphereio/predictionio

ADD RecommendationEngine /RecommendationEngine

EXPOSE 8000

ADD run.sh /run.sh

ENTRYPOINT /run.sh
