FROM sphereio/predictionio

ADD RecommendationEngine /RecommendationEngine

COPY lib/sbt-launch-0.13.8.jar /PredictionIO-0.9.3/sbt/sbt-launch-0.13.8.jar

COPY project/build.properties /PredictionIO-0.9.3/project/build.properties

EXPOSE 8000

ADD run.sh /run.sh

ENTRYPOINT /run.sh
