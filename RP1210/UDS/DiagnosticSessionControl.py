from . import UDSMessage

class DiagnosticSessionControlRequest(UDSMessage):
    """
    Diagnostic Session Control (Request)
    - `sid` = 0x10
    - `subfn` = diagnosticSessionType
    """
    _sid = 0x10

    _isResponse = False

    _hasSubfn = True
    _hasDID = False
    _hasData = False

    # sub-function IDs, for convenience:
    defaultSession = 0x01
    programmingSession = 0x02
    extendedDiagnosticSession = 0x03
    safetyDiagnosticSession = 0x04

    def __init__(self, subfn : int = defaultSession):
        self.subfn = subfn

class DiagnosticSessionControlResponse(UDSMessage):
    """
    Diagnostic Session Control (Response)
    - `sid` = 0x50
    - `subfn` = diagnosticSessionType
    - `data` = sessionParameterRecord (4 bytes)
       1. P2Server_Max (high)
       2. P2Server_Max (low)
       3. P2*Server_Max (high)
       4. P2*Server_Max (low)
    """

    _sid = 0x50

    _isResponse = True

    _hasSubfn = True
    _hasDID = False
    _hasData = True
    _dataSize = 4
    _dataSizeCanChange = False

    # sub-function IDs, for convenience:
    defaultSession = 0x01
    programmingSession = 0x02
    extendedDiagnosticSession = 0x03
    safetyDiagnosticSession = 0x04

    def __init__(self, subfn : int = defaultSession, data : bytes = b''):
        self.subfn = subfn
        self.data = data

