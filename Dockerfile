FROM sphereio/predictionio

ADD RecommendationEngine /RecommendationEngine
COPY lib/sbt-launch-0.13.8.jar /PredictionIO-0.9.3/sbt/sbt-launch-0.13.8.jar
COPY project/build.properties /PredictionIO-0.9.3/project/build.properties

VOLUME /PredictionIO-0.9.3/vendors/elasticsearch-1.4.4/data/
VOLUME /PredictionIO-0.9.3/vendors/hbase-1.0.0/data/
EXPOSE 8000 7070 9000

ADD run.sh /run.sh

ENTRYPOINT /run.sh
