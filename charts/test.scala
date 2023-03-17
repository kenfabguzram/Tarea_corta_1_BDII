import io.gatling.core.Predef._
import io.gatling.http.Predef._
import io.gatling.jdbc.Predef._
import com.mongodb.client.MongoClients
import org.bson.Document

class MongoSimulation extends Simulation {

  val uri = "mongodb://localhost:27017"
  val client = MongoClients.create(uri)
  val database = client.getDatabase("test")
  val collection = database.getCollection("users")

  val httpProtocol = http
    .baseUrl("http://localhost:8080")
    .acceptHeader("application/json")

  val scn = scenario("MongoDB Test")
    .exec(
      session => {
        val document = new Document()
          .append("name", "John Doe")
          .append("email", "johndoe@example.com")
        collection.insertOne(document)
        session
      }
    )
    .exec(
      http("Get User")
        .get("/users/1")
        .check(jsonPath("$.name").is("John Doe"))
    )
    .exec(
      session => {
        collection.deleteOne(new Document("name", "John Doe"))
        session
      }
    )

  setUp(scn.inject(atOnceUsers(1))).protocols(httpProtocol)
}
