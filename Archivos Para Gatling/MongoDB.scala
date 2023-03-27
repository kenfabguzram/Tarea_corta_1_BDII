//LEER COMENTARIOS EN EL DOCUMENTO IMPORTANTE
import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

//Agregar este archivo dentro de la carpeta simulations de Gatling
class MongoDB extends Simulation {

  val httpConf = http
    .baseUrl("http://localhost:30000") //Url de la app Flask
    .acceptHeader("application/json")

  val scn = scenario("Enviar JSON a Flask")
    .exec(http("POST JSON")
      .post("/mongodb/post") //Tener en cuenta que para mongodb tambien esta la ruta /mongodb/get
      .body(StringBody("""{
        "animales": [
          {
            "Tipo": "Perro",
            "Nombre": "Max"
          },
          {
            "Tipo": "Gato",
            "Nombre": "Manchas"
          },
          {
            "Tipo": "Perro",
            "Nombre": "Bruno"
          }
        ],
        "host": "(Aqui tiene que ir el clusterip del servicio de mongodb)"
      }""")).asJson  //Todo ese texto es el JSON que se va a enviar, se puede modificar para hacerlo como se desee
      .check(status.is(200)))

  setUp(
    scn.inject(
      constantUsersPerSec(5) during (120 seconds) //Cantidad de usuarios que realizaran request por segundo, estos pueden ser modificados
    )
  ).protocols(httpConf)

}