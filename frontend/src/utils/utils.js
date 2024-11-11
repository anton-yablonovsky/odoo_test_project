import axios from "axios";

async function checkAccess() {
  await axios
    .get("users/check_access/")
    .then((response) => {
      if (!response.data.isAccess) {
        alert("Access denied!")
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

export {
    checkAccess,
}  
