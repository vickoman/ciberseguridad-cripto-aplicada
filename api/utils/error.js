const raiseError = (status, message) => {
    const error = new Error(message);
    error.statusCode =  status;
    return error;
}
module.exports = raiseError;